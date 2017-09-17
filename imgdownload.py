#!/usr/bin/python
import os
import sys
import urllib2
from urllib import urlretrieve
import urlparse
import json
import re


pattern_image = re.compile("\.\w+$")

def download(i, data, directory):
    filename = "image" + str(i)
    outpath = os.path.join(directory, filename)
    f = open(directory + "image"+ str(i)+".jpg", 'wb')
    img = urllib2.urlopen(data["url"])
    f.write(img.read())


def main():
    print "This program will download 20 pictures from r/wallpaper and save to the images directory\n"

    image_extensions = ["jpg", "jpeg", "png"]

    # create directory to save images to if it does not already exist
    directory = "images/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Set custom User-Agent to allow request to be sent
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    # Request the url and retreive the webpage
    req = urllib2.Request('https://www.reddit.com/r/wallpaper/', None, headers)
    html = urllib2.urlopen(req).read()

    response = urllib2.urlopen('http://www.reddit.com/r/wallpaper' + '/hot/.json?limit=' + '50')    # download 20 images from "hot" category
    data = json.load(response)

    i = 1
    for element in data["data"]["children"]:
        if pattern_image.search(element["data"]["url"]):
            if element["data"]["url"].split(".")[-1] in image_extensions:
                print "Downloading image " + str(i) + "..."
                download(i, element["data"], directory)
                i += 1
        if i > 20:
            break
    print "Download complete."

if __name__ == "__main__":
    main()
