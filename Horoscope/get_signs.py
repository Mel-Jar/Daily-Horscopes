import daily_horscope

def parser(soup, horscopes):
    scopes = soup.find_all("a", class_="module-skin flex-2 sign-teasers__item")
    num = 1
    for scope in scopes:
        sign = scope.find("h3")
        daily_horscope.parser(sign.text, num, horscopes)
        num += 1
        
