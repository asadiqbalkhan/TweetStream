@echo off
REM change directory to the folder containing python script
cd /d C:\Project
REM execute the python script
python tweetfetch.py
REM Access VM and move the json files to processed folder
pscp -pw "***************" C:\Project\*.json root@192.168.101.138:/root/tweet_received && move C:\Project\*.json C:\processed
