# -*- coding: utf-8 -*-
"""
Created on Sun May  1 16:12:11 2016
@author: debverine
"""
import http.client
import pygame.mixer
import time

#1
def have_internet():
    conn = http.client.HTTPConnection("www.google.com")
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False
    

#2
mixer.init()
s=mixer.music
s.load("E:\Songs\VA-Rocky_Balboa_The_Best_Of_Rocky-OST-(Advance)-2006-RTB\song.mp3")
#s.play()
#s.stop()

start=time.time()
end=start+3600
i=1
while(time.time()<=end):
    print (i)
    i+=1
    if have_internet()==False:
        s.play()
    else:
        s.stop()
    time.sleep(3)