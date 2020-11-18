#!/usr/bin/python

import pafy
import sys
import time

# Seetting api key
pafy.set_api_key('AIzaSyAhCAsK0kBJtd24kbxs2YwkeCETETrcAIo')


def main():

    # URL for just2good's list of videos
    url = 'https://www.youtube.com/playlist?list=UUp_mZttcKNIcUBVdi0wTdIA'

    # Open file to retrieve previous count
    prevFile = open('previous.txt', 'r')

    # Setting the previous count
    prevCount = int(prevFile.read())
    prevFile.close()

    # Creating playlist object and current count
    playlist = pafy.get_playlist2(url)
    currCount = len(playlist)

    # If new videos have been added, download the most recent ones
    if (currCount > prevCount):
        for i in range(0, currCount - prevCount):
            print("Downloading...'" + playlist[i].title + "'")
            playlist[i].getbest().download()

    # Clearing the plalist object
    playlist = None

    # Clearing previous value and adding new previous value
    prevFile = open('previous.txt', 'w')
    prevFile.truncate()
    prevFile.write(str(currCount))

    # Closing the file
    prevFile.close()




if __name__ == '__main__':
    main()
