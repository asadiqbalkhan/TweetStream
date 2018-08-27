REGISTER hdfs:///usr/json-serde-1.3.8.jar;
a = LOAD 'raw_tweets_tbl' USING org.apache.hive.hcatalog.pig.HCatLoader();
f = FOREACH a GENERATE ToDate(created_at,'EEE MMM dd HH:mm:ss Z yyyy') as
(date_time:DateTime),id as iden, text as t;
y = FOREACH f GENERATE
GetYear(date_time) as (year:chararray),
GetMonth(date_time) as (month:chararray),
GetDay(date_time) as (day:chararray),
GetHour(date_time) as (hour:chararray),
GetMinute(date_time) as (minute:chararray),
iden as (id:chararray),
t as (text:chararray);

STORE y INTO 'proc_tweets_tbl' USING org.apache.hive.hcatalog.pig.HCatStorer();
