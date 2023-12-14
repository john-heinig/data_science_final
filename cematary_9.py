import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup
import re


# this script reads in everything from the first retrosheet 
df = pd.DataFrame()
data = pd.DataFrame()
df = pd.read_csv("biofile.csv", usecols= ["PLAYERID","CEMETERY","LAST","FIRST","NICKNAME","BIRTHDATE","BIRTH.CITY","CEME.CITY","CEME.STATE","CEME.COUNTRY","CEME.NOTE","BIRTH.NAME","NAME.CHG","BAT.CHG","HOF","DEATHDATE"])

#print(len(df.index))
df = df.dropna(subset=["CEMETERY"])
df = df.dropna(subset=["DEATHDATE"])
#for ind in df.index:
#    if df["CEME.NOTE"][ind]:
#        df.drop(index=ind)

data["CEME.NOTE"] = df["CEME.NOTE"]

#print(data["CEME.NOTE"])



print(len(df.index))

df.to_csv("test.csv")







