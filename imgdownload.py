#!/usr/bin/python
import os
import sys
import urllib2
from BeautifulSoup import BeautifulSoup as bs
from urllib import urlretrieve
import urlparse

def main():
    print "This program will download 20 pictures from r/wallpaper and save to the images directory\n"
    
    # create directory to save images to if it does not already exist
    directory = "images/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    ## download the page and parse html document, find your image with regex and download it
    ## use urllib2 for downloading and Beautiful Soup for parsing html file.

    # Set custom User-Agent to allow request to be sent
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    # Request the url and retreive the webpage
    req = urllib2.Request('https://www.reddit.com/r/wallpaper/', None, headers)
    html = urllib2.urlopen(req).read()

    soup = bs(urllib2.urlopen(req))

    i = 0
    for image in soup.findAll("img"):
        print "Image: %(src)s" % image
        filename = "image" + str(i)
        outpath = os.path.join(directory, filename)
        i = i + 1

if __name__ == "__main__":
    main()
