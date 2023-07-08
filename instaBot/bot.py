#!/usr/bin/python3
import os
from dotenv import load_dotenv
from instagrapi import Client


load_dotenv()

USERNAME = os.getenv('USERNAME')
PASS = os.getenv('PASS')

hashtag = 'programming'

# login
user = Client()
status = user.login(USERNAME, PASS)
if status == True:
    print("logged in")


# Return Top posts by Hashtag, return type = list
medias = user.hashtag_medias_top(hashtag, amount=5)

print(medias[0].dict())
