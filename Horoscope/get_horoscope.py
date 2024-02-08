from bs4 import BeautifulSoup
import json 
import requests
import importlib
import sys
import get_signs

def main():
    sign = "Libra"
    horscopes = {}
    URL = "https://www.horoscope.com/us/horoscopes/general/index-horoscope-general-daily.aspx"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    get_signs.parser(soup, horscopes)
    print("Here is your Daily Horscope for" + sign + ":")
    print(horscopes[sign])
main()