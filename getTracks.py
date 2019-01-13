# spotify: BQAZNW0EngusX8ZI1ZY6AOd9M9nVZeTvyJH2QSy2RI46JqPvFxBtBr1QQn9BgarTmq6X6pmTt2k1mCTvtrp1SFCGz-nZ4UiwAXh9a8fO04U0Qxvb2Nvp55cwx2UwtSaSXzEV3Xw9n3HJJrhH9w

import json, requests
from pprint import pprint

with open('weekList.json') as dataFile:
	weekList = json.load(dataFile)

allWeeks = {}

# for i in (weekList['weeklychartlist']['chart']):
# 	singleWeek = []
# 	startDate = i['from']
# 	endDate = i['to']
	
# 	url = "http://ws.audioscrobbler.com/2.0/?method=user.getweeklytrackchart&user=rchlchang&from="+startDate+"&to="+endDate+"&api_key=4cee3d3350169472f7c3f49118dd2bb1&format=json"
# 	response = requests.get(url)

# 	if (len(response.json()['weeklytrackchart']['track'])==0):
# 		print i
# 		continue
# 	else:
# 		for a in response.json()['weeklytrackchart']['track']:
# 			track = {}
# 			track["Count"] = int(a['playcount'])
# 			track["Title"] = a['name'].encode('utf-8')
# 			track["Artist"] = a['artist']['#text'].encode('utf-8')
			
# 			singleWeek.append(track)
# 		allWeeks[startDate] = singleWeek

# with open('tracksPerWeek2.json', 'w') as outfile:  
#     json.dump(allWeeks, outfile)

with open('tracksPerWeek.json') as dataFile:
	allTracks = json.load(dataFile)

print allTracks['1528027200']


"https://api.spotify.com/v1/search?q=track:'"+title+"'&artist:'"+artist+"'&type='track'"

# for each week:
# 	look up song, 
# 	add valence*trackcount
# 	add trackcount
# 	valence/trackcount

