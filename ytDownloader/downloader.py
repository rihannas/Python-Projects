#!/usr/bin/python3
"""This script downloads youtube videos into your downloads using the linm of the video"""
from pytube import YouTube
from sys import argv

link = argv[1]

vidObj = YouTube(link)

print("Title: ", vidObj.title)
print("Views: ", vidObj.views)


vid = vidObj.streams.get_by_resolution("720p")
vid.download('Users/Rihannas/Downloads')
print('download is ready')
