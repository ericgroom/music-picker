#!/usr/bin/env python3
from random import randint
import webbrowser

PLAYLIST_LEN = 115
PLAYLIST_ID = "PL_VhV5m_X3BK-j1rqyOG5j7FraqSEIxVw"
AUTOPLAY = 1
URL_FORMAT = "https://www.youtube.com/embed?listType=playlist&list=%s&index=%s&autoplay=%s"

index = randint(0, PLAYLIST_LEN-1)

url = URL_FORMAT % (PLAYLIST_ID, index, AUTOPLAY)

webbrowser.open(url, new=1)