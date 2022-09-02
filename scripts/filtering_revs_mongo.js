/*
    * *** Cleaning of the small_reviews collection data stored in the MongoDB repository ***
    * 
    * The reviews records extracted from the data source contain incoherent data. This script:
    *     - removes records with playtime_forever < playtime_at_review (it should be impossible);
    *     - removes records with null/empty text reviews.
    * 
    * How to run this script:
    * $ mongosh -f filtering_revs_mongo.js
*/

// Connect to the MongoDB instance and select the final_project database
db = connect('mongodb://localhost/final_project');

// Remove the small_reviews_filtered collection if it already exists
db.small_reviews_filtered.drop({});

// Create the collection small_reviews_filtered with the filtered data from small_reviews
db.small_reviews.aggregate([
    {
        $match: {
            // Combine multiple checks on relevant fields
            $and: [
                // Filter out the null/empty text reviews
                {review: {$ne: null}},
                {review: {$ne: ''}},

                // Filter out the reviews with a negative playtime after review
                {$expr: {$gte: ['$playtime_forever', '$playtime_at_review']}}
            ]
        }
    },

    // Store the result of the filtering in the small_reviews_filtered collection
    {$out: 'small_reviews_filtered'}
]);
