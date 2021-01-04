#!/usr/bin/env python3

"""
Author : GordonWei
Date : 01/04/21
Comment : Get Expire Data (3 Days Ago)And Delete It Automation.
HowToUse : Using Crontab To Trigger.
"""


import requests, subprocess
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta, date

# Get Today Time
today = date.today() - timedelta(days=1)
today = today.strftime('%Y.%m.%d')

# Get Kibana Index Pattern.
getIndex = requests.get("http://kibanaURL:9200/_cat/indices?v&h=i", auth = HTTPBasicAuth('elastic', 'ChangeMe'))
writeFile = open('./456', 'w')
writeFile.writelines(getIndex.text)
writeFile.close()

# Filter Keyword 
subprocess.call('cat 456 | grep ' + today + ' > 123', shell = True)

# Read Filter File And Request With Delete Functoin To Clean Index Pattern
readFile = open('./123', 'r')
readLines = readFile.readlines()
for line in readLines:
  print(line)
  line = line.replace('\n','')
  requests.delete('http://kibanaURL:9200/'+ line, auth = HTTPBasicAuth('elastic', 'ChangeMe'))
