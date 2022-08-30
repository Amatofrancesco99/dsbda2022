/*
*****  CLEANING REVIEWS DATA WITH A COMLPEX MongoDB QUERY *****

OBJECTIVE:
It has been noticed that the data in our Data Source are not clean as expected, so some filtering has been applied to the following fields:
    - negative playtime_after_review (playtime_forever - playtime_at_review)...how's possible?
    - review with empty/null written text

HOW TO RUN IT? 
Execute in the same folder of this script the following command in terminal/bash
    % mongosh < filtering_revs_mongo.js
*/


// Move to final project MongoDB
use final_project

// Remove small_reviews_filtered collection if already exists
db.small_reviews_filtered.drop({})

// Create a new collection named small_reviews_filtered, filtering the data of the small_reviews collection
db.small_reviews.aggregate(
    [
        {
            $match: {
                // Combine multiple checks on chosen fields
                $and:
                    [
                        // Filter on empty/null text reviews
                        { 'review': { $ne: null } }, { 'review': { $ne: '' } },
                        // Filter on negative playtime_after_review
                        { $expr: { $gte: ['$playtime_forever', '$playtime_at_review'] } }
                    ]
            }
        },
    // Store the filtering result in the small_reviews_filtered collections
    { $out: 'small_reviews_filtered' }
    ]
)