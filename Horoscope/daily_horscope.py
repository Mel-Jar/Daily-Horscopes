from bs4 import BeautifulSoup
import requests

def parser(sign, num, horscopes):
    URL = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="+str(num)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    scopes = soup.find("p")
    for scope in scopes:
        final_scope = scope
    horscopes[sign] = final_scope.text
    