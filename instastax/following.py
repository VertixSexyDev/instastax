import requests
from bs4 import BeautifulSoup

def following(username):

    url = "https://www.instagram.com/" + username

    r = requests.get(url)

    s = BeautifulSoup(r.text, "html.parser")

    u = s.find("meta", property="og:description")

    info = u.attrs['content']

    info_list = list([int(word) for word in info.split() if word.isdigit()])

    following_num = [info_list[1]]
    following = print(following_num)
    return following
