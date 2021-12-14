import requests
from bs4 import BeautifulSoup

def posts(username):

    url = "https://www.instagram.com/" + username

    r = requests.get(url)

    s = BeautifulSoup(r.text, "html.parser")

    u = s.find("meta", property="og:description")

    info = u.attrs['content']

    info_list = list([int(word) for word in info.split() if word.isdigit()])

    posts_num = [info_list[2]]
    posts = print(posts_num)
    return posts
