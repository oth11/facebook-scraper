import requests
import sys
import os
import datetime
import pandas as pd

from facebook_scraper import get_posts

# use argument 1 with your list (text file with 1 page per line) and argument 2 with your cookies.txt from FB (using get cookies.txt plugin)
list_file = sys.argv[1]     #list as text file
cookie_file = sys.argv[2]   #your cookies from FB
no_pages = 3                #no. of pages to scrape
userids = []                #empty all userids 
fb_path = ".../"            #set your own path to write files

# get date - used to write filenames
now = datetime.datetime.now()
date_string = str(now.date())
print(date_string)          #screen output of date

# get all pages to scrape
with open(list_file, 'r') as targets_file:
  targets_list = targets_file.readlines()
for item in targets_list:
  userids.append(item.strip('\n'))

def get_page_posts(ID):
  filename_csv = fb_path + date_string + '-' + ID + '.csv'
  allposts = pd.DataFrame(data = get_posts(ID, cookies=cookie, pages=no_pages))
  print(allposts)
  allposts.to_csv(filename_csv, index=False)

if __name__ == '__main__':
  #pass in the username of the account you want to download
  for x in userids:
    
    #the following lines can be used to change the ip address with every call using the tor network
    os.system("sudo echo -e 'AUTHENTICATE ""\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051")
    ip = os.system("sudo /home/ubuntu/./usetor.sh")
    print(ip)               #screen ouput of ip address used
    #end tor
    
    print(x)                #screen output of FB page name
    get_page_posts(x)
