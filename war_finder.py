import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup
import re
import time
import json
import datetime
from pybaseball import playerid_lookup, playerid_reverse_lookup
import http.client
#with open("cem_dict.json", "w") as f:
#    json.dump(cems_dict, f, indent=4)
starttime = datetime.datetime.now()

print(starttime)

# this script reads the data in from player_data.csv then stores it in a dictionary with each cemetery as a key 
# and each playerid and last name of a player buried in that cemetery as a value

# then it iterates through the dict and looks up each players WAR in the find_war function by scrapping
# baseball reference

# the final dictionary is stored in cem_dict.json
df = pd.DataFrame()
df = pd.read_csv("player_data.csv")
cems = set()
cems_dict = {}

for ind in df.index:
    cems.add(str(df["CEMETERY"][ind]) + str(df["CEME.CITY"][ind]))

for x in cems: 
        cems_dict.__setitem__(x,[])

for ind in df.index:
      if (str(df["CEMETERY"][ind]) + str(df["CEME.CITY"][ind])) in cems:
            cems_dict[str(df["CEMETERY"][ind]) + str(df["CEME.CITY"][ind])].append((df["PLAYERID"][ind] , df["LAST"][ind]))

del_keys = []
for key in cems_dict:
      if len(cems_dict[key]) < 11 or len(cems_dict[key]) > 100:
            del_keys.append(key)

for x in del_keys:
      del cems_dict[x]
#print(cems_dict)

key_count = 0
count = []
len_lst = []
for keys in cems_dict:
    count.append(len(cems_dict[keys]))
    len_lst.append((len(cems_dict[keys]),keys))
    key_count+=1

players = sum(count)
print(" there are " + str(key_count) + " cemeterys")
print(" and there are " + str(players) + " players")
players = players/20
print("so at 20 players every minute it will take " + str(players) + " minutes ")

#with open("cem_dict.json", "w") as f:
#    json.dump(cems_dict, f,indent=1)

legal_scraper = 0
x = 6

def find_war(name):
    global legal_scraper
    global x

    lname = name[1].lower()
    
    time.sleep(x%5)
    x += 1
   

    
    legal_scraper += 1

   
    
    url = "https://www.baseball-reference.com/" + lname[0] + "/" + name[0] + ".shtml"
    response = requests.get(url)
    if response.status_code == 200:
        player_soup = BeautifulSoup(response.text, 'html.parser')
    elif response.status_code == 429:
        with open("cem_dict.json", "w") as f:
            json.dump(cems_dict, f, indent=4)
        print("429d")
        exit()
    else:
        return -5.0
    player_soup = (player_soup.find("div", class_="p1")).find("p")
    war = player_soup.getText()
    return war
    
x = 0
for keys in cems_dict:
    

    print(len(cems_dict[keys]))
    for names in cems_dict[keys]:
        #print(type(cems_dict[keys][names]))
        #last_name = names[0].split(" ")[0]
        #print(names[0])
        i = cems_dict[keys].index(names)
        bad_names = []
        if legal_scraper < 12:
            try:
                cems_dict[keys][i] = (names[1], find_war(names))
                with open("cem_dict.json", "w") as f:
                    json.dump(cems_dict, f, indent=4)
                #print(legal_scraper)
            except http.client.HTTPException:
                with open("cem_dict.json", "w") as f:
                    json.dump(cems_dict, f, indent=4)
                print("429d")
                exit()
                       
        else:
            time.sleep(61)
            legal_scraper = 0
    #x+=1
    
    #if x == 20:
     #   with open("cem_dict.json", "w") as f:
     #       json.dump(cems_dict, f, indent=4)
     #   print("done")
     #   exit()
         
         


             
    #print(cems_dict[keys])

with open("cem_dict.json", "w") as f:
    json.dump(cems_dict, f, indent=4)
starttime = datetime.datetime.now()

print(starttime)
#find_war("Aaron Henry")

#print(key_count)
#print(len_lst)
#print(cems_dict.keys)
#print(len(df.index))
#df.to_csv("test.csv")
#with open("test.csv","w"):