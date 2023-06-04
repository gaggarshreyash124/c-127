from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Edge("C:\Users\frame\Downloads\chromedriver_win32")
browser.get(starturl)
time.sleep(10)

def scrap():
    headers = ["name","lightyearsfromearth","planatmass","stellarmagintude","discoverydate"]
    planetdata = []
    soup = BeautifulSoup(browser.page_source)
    for ultag in  soup.find_all("ul"): 
        litag=ultag.find_all("li")
        templist = []
        for index,litag in enumerate(litag):
            if index == 0:
                templist.append(litag)
            else:
                try:
                    templist.append(litag.contents[0])
                except:
                    templist.append("")
        
        planetdata.append(templist)

    with open("space.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)

scrap()