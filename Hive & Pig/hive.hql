add jar hdfs:///usr/json-serde-1.3.8.jar;
SET hive.support.sql11.reserved.keywords=false;
LOAD DATA IN PATH '/usr/tweet_received'
OVERWRITE INTO TABLE raw_tweets_tbl;
