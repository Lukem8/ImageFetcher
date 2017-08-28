#!/usr/bin/python

import urllib2


def main():
    print "This program will download 20 pictures from r/wallpaper"

    ## download the page and parse html document, find your image with regex and download it
    ## use urllib2 for downloading and Beautiful Soup for parsing html file.

    # Set custom User-Agent to allow request to be sent
    headers = { 'User-Agent' : 'Mozilla/5.0' }

    # Request the url and retreive the webpage
    req = urllib2.Request('https://www.reddit.com/r/wallpaper/', None, headers)
    html = urllib2.urlopen(req).read()






if __name__ == "__main__":
    main()
