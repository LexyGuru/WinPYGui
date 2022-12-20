import json
import tkinter as tk
from tkinter import *
import os
import sys
from tkinter import messagebox
from tkinter import Tk, Button, Frame
from tkinter.scrolledtext import ScrolledText
from bs4 import BeautifulSoup as bs
import requests

ws = Tk()
ws.title('Media Server List')
ws.geometry('400x300')

var = StringVar()
response = open('../config.json', encoding='utf-8')
data_jsonq = json.loads(response.read())

def configure():
    import subprocess as sp
    programName = "notepad.exe"
    fileName = "../config.json"
    sp.Popen([programName, fileName])

lang = (data_jsonq['config_language'][0])

path = 'language/' + lang + '.json'
isFile = os.path.isfile(path)
#print(isFile)

if isFile == True:
    language = 'language/' + lang + '.json'
    response = open(language, encoding='utf-8')
    data_lang_json = json.loads(response.read())

else:
    messagebox.showwarning("Warning", "'" + lang + "'" + " Language File Not Found!!!")

def ido():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    # US english
    LANGUAGE = data_jsonq['language_weather'][0]
    locat = data_jsonq['locations'][0]

    # data_lang_json[lang][0]['Menu']['Version']
    # data_jsonq['language_weather'][0]

    def get_weather_data(url):
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        html = session.get(url)
        # create a new soup
        soup = bs(html.text, "html.parser")
        # store all results on this dictionary
        result = {}
        # extract region
        result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
        # extract temperature now
        result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
        # get the day and hour now
        result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
        # get the actual weather
        result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
        # get the precipitation
        result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
        # get the % of humidity
        result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
        # extract the wind
        result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
        # get next few days' weather
        next_days = []
        days = soup.find("div", attrs={"id": "wob_dp"})
        for day in days.findAll("div", attrs={"class": "wob_df"}):
            # extract the name of the day
            day_name = day.findAll("div")[0].attrs['aria-label']
            # get weather status for that day
            weather = day.find("img").attrs["alt"]
            temp = day.findAll("span", {"class": "wob_t"})
            # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
            max_temp = temp[0].text
            # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
            min_temp = temp[2].text
            next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
        # append to result
        result['next_days'] = next_days
        return result

    if __name__ == "__main__":
        URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather+" + locat
        import argparse
        parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
        parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                            Default is your current location determined by your IP Address""",
                            default="")
        # parse arguments
        args = parser.parse_args()
        region = args.region
        if region:
            region = region.replace(" ", "+")
            URL += f"+{region}"
        # get data
        data = get_weather_data(URL)
        # print data

        a = (data_lang_json[lang][0]['Weather']['Weather_for'], data["region"])
        aa = (data_lang_json[lang][0]['Weather']['Now'], data["dayhour"])
        print(data_lang_json[lang][0]['Weather']['Temperature_now'], f"{data['temp_now']}°C")
        print(data_lang_json[lang][0]['Weather']['Description'],data['weather_now'])
        print(data_lang_json[lang][0]['Weather']['Precipitation'],data["precipitation"])
        print(data_lang_json[lang][0]['Weather']['Humidity'],data["humidity"])
        print(data_lang_json[lang][0]['Weather']['Wind'],data["wind"])
        print(data_lang_json[lang][0]['Weather']['Next_days'])


        for dayweather in data["next_days"]:
            print("\r")
            print("=" * 40, dayweather["name"], "=" * 40)
            print(data_lang_json[lang][0]['Weather']['Description'], dayweather["weather"])
            print(data_lang_json[lang][0]['Weather']['Max_temperature'], f"{dayweather['max_temp']}°C")
            print(data_lang_json[lang][0]['Weather']['Min_temperature'], f"{dayweather['min_temp']}°C")

ido()