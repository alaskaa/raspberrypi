#!/usr/bin/python

import tweepy
import os
import picamera
import time

auth = tweepy.OAuthHandler('X', 'X')

auth.set_access_token('X', 'X')

twitter_api = tweepy.API(auth)

camera = picamera.PiCamera()
camera.capture('test1.jpg')
time.sleep(1)

photo = '/home/pi/test1.jpg'
status = 'This is a test using the Raspberry Pi Camera module via Tweepy!'
twitter_api.update_with_media(photo,status=status)
