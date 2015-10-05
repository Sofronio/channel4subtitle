'''
import urllib2
subfile = urllib2.urlopen("http://ais.channel4.com/subtitles/3612329")
output = open('3612329.txt','w+b')
#output = open('3612329.txt','w+b')
output.write(subfile.read())
output.close()
'''

'''
import xml.etree.ElementTree as ET
tree = ET.parse('jamies-super-food.xml')
root = tree.getroot()
for episodeList in root.findall('episodeList'):
  requestId = episodeList.find('requestId')
  print requestId
'''


import xml.etree.ElementTree as ET
import urllib2
import os
import sys

xmlfile = sys.argv[1]
subtitles_list = list()
tree = ET.parse(xmlfile)
root = tree.getroot()
title = root.find('title')

for episode in root.iter(tag='episode'):
    if episode.find('subtitled').text == 'false':
        continue
    subtitle_list = ['', '', '', '', '', '']
    #title, season, episode, subtitle_requestId, title, thumbnail
    subtitle_list[0] = title.text
    subtitle_list[1] = episode.find('seriesNumber').text
    subtitle_list[2] = episode.find('episodeNumber').text
    subtitle_list[3] = episode.find('requestId').text
    subtitle_list[4] = episode.find('title1').text
    subtitle_list[5] = episode.find('pictureComponent').find("url").text
    subtitles_list.append(subtitle_list)

for plainsub in subtitles_list:
    subfile = urllib2.urlopen(
        "http://ais.channel4.com/subtitles/" + plainsub[3])
    path = "\\" + plainsub[0] + "\\" + 'Series ' + \
        plainsub[1] + ' Episode ' + plainsub[2] + "\\"
    subfilename = 'Series ' + \
        plainsub[1] + ' Episode ' + plainsub[2] + ' - ' + plainsub[4]
    if os.path.isdir(os.getcwd() + path):
        pass
    else:
        os.makedirs(os.getcwd() + path)
    output = open(os.getcwd() + path + subfilename + '.txt', 'wb')
    output.write(subfile.read())
    output.close()
    print os.getcwd() + path + subfilename

    print plainsub[5]
    imgfile = urllib2.urlopen(plainsub[5])
    output = open(os.getcwd() + path + subfilename + '.jpg', 'wb')
    output.write(imgfile.read())
    output.close()

    print 'Write Complete\n'
