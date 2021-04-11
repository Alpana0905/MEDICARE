import folium

import requests

r = requests.get('https://get.geojs.io/')

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()['ip']

url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
geo_request = requests.get(url)
geo_data = geo_request.json()
latitude = geo_data['latitude']
longitude = geo_data['longitude']

fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[latitude, longitude],popup=" user's location "))

map=folium.Map(location=[21.1458,79.0882],zoom_start=5)

map.add_child(fg)
map.save("test.html")

# print("latitude : ",geo_data['latitude'])
# print("longitude : ",geo_data['longitude'])
# print("city : ",geo_data['city'])
# print("region : ",geo_data['region'])
# print("country : ",geo_data['country'])





