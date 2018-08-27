SET hive.support.sql11.reserved.keywords=false;
CREATE EXTERNAL TABLE IF NOT EXISTS raw_tweets_tbl(created_at string,
id string, id_str string, text string, source string, truncated string,
user struct< id:string, id_str:string, name:string, screen_name:string,
location:string, url:string,description:string, translator_type:string,
protected:string, verified:string, followers_count:string,
friends_count:string, listed_count:string, favourites_count:string,
created_at:string, utc_offset:string,time_zone:string>)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' STORED AS TEXTFILE;
