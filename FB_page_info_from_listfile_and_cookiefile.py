#script will check a list of pages for page info and write a csv file for each facebook page

import requests
import sys
import os
import datetime
import pandas as pd

from facebook_scraper import get_page_info

# use argument 1 with your list (text file with 1 page per line) and argument 2 with your cookies.txt from FB (using get cookies.txt plugin)
list = sys.argv[1]    #list as text file
cookie = sys.argv[2]  #your cookies from FB

# get date - used to write filenames
now = datetime.datetime.now()
date_string = str(now.date())
print(date_string)  #screen output of date

userids = []  #empty all userids 
fb_path = ".../" #set your own path to write files

# get all pages to scrape
with open(list, 'r') as targets_file:
  targets_list = targets_file.readlines()
for item in targets_list:
  userids.append(item.strip('\n'))

# scrape page info
def page_profile(ID):
  filename_csv = fb_path + date_string + '-' + ID + '-info.csv' #set file name
  profile = pd.DataFrame(data = get_page_info(ID, cookies=cookie), index=[0])
  profile.to_csv(filename_csv, index=True)

if __name__ == '__main__':
  for x in userids:
    #the following lines can be used to change the ip address with every call using the tor network
    os.system("sudo echo -e 'AUTHENTICATE ""\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051")
    ip = os.system("sudo /home/ubuntu/./usetor.sh")
    print(ip) #screen ouput of ip address used
    
    print(x)  #screen output of FB page name
    page_profile(x)
