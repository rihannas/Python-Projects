#!/usr/bin/python3
import json
import os
from dotenv import load_dotenv 
from base64 import b64encode
from requests import post, get

load_dotenv() #helps on loading or .env variables

# actually gets the values from the .env variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# we need to get an access token, which will allows us 
# to send requests for the things we want like artists, playlists 
# to get this token we need to send the auth string according to
# the doc of the spotify web api

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(b64encode(auth_bytes), 
                      "utf-8")
    
    # the destination we will send our request to
    url = 'https://accounts.spotify.com/api/token'

    # headers a dicts
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-type": "application/x-www-form-urlencoded"
    }

    # the type of data we are sending, matters as the response will depend on the message we are sending
    data = {"grant_type": "client_credentials"}

    # sending a post request
    # this will return a resonse object, where we can access the content by using the .content attribute
    response = post(url, headers=headers, data=data)
    json_result = json.loads(response.content)
    token = json_result["access_token"]
    return token


    # returns the token as a part of the auth header
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_artist(token, artist):
    url = 'https://api.spotify.com/v1/search?'
    headers = get_auth_header(token)
    query = f"q={artist}&type=artist&limit=1"

    query_url = url + query

    response = get(query_url, headers=headers)
    json_result = json.loads(response.content)["artists"]["items"]

    if len(json_result) == 0:
        print("no artist with this name exists...")
        return None
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)

    response = get(url, headers=headers)
    json_result = json.loads(response.content)["tracks"]
    return json_result



token = get_token()
result = search_artist(token, "bts")
artist_id = result["id"]

songs = get_songs_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")