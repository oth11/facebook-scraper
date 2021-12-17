import requests
import sys
import os
import csv
import json
import datetime
import pandas as pd

from json import JSONEncoder
from facebook_scraper import get_posts

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

# use argument 1 with your list (text file with 1 profile per line) and argument 2 with your cookies.txt from FB

list = sys.argv[1]    #list as text file
cookie = sys.argv[2]  #your cookies from FB

no_pages = 3          #no. of pages to scrape

now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d')
print(date_string)

with open(list, 'r') as targets_file:
  targets_list = targets_file.readlines()

userids = []
lines = []

for item in targets_list:
  userids.append(item.strip('\n'))

def get_page_posts(userid):
  allposts = pd.DataFrame(data = get_posts(userid, cookies=cookie, pages=no_pages))
  print(allposts)
  allposts.drop(allposts.index, inplace=True)
  for post in get_posts(userid):
    # write json
    filename = 'folder' + date_string + userid + '.txt'  #filename is set to date + userid, folder can be set. delete for root folder
    f = open(filename, 'a')
    postJSONData = json.dumps(post, indent=4, cls=DateTimeEncoder)
    f.write(postJSONData)
    f.close()

if __name__ == '__main__':
  #pass in the username of the account you want to download
  for x in userids:
    
    #the following lines can be used to change the ip address with every call using the tor network
    os.system("sudo echo -e 'AUTHENTICATE ""\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051")
    ip = os.system("sudo /home/ubuntu/./usetor.sh")
    print(ip)
    #end tor
    
    print(x)
    get_page_posts(x)
