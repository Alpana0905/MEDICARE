from django.shortcuts import render
import requests

def button(request):
  return render(request,'home.html')

def output(request):
  r = requests.get('https://get.geojs.io/')

  ip_request = requests.get('https://get.geojs.io/v1/ip.json')
  ipAdd = ip_request.json()['ip']

  url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
  geo_request = requests.get(url)
  geo_data = geo_request.json()
  latitude = geo_data['latitude']
  longitude = geo_data['longitude']

  print("latitude : ",geo_data['latitude'])
  print("longitude : ",geo_data['longitude'])
  print("city : ",geo_data['city'])
  print("region : ",geo_data['region'])
  print("country : ",geo_data['country'])

  # data = {'latitude' : geo_data['latitude'],'longitude ': geo_data['longitude'],'city' : geo_data['city'],'region' : geo_data['region'],'country' : geo_data['country']}

  data = geo_request.text
  return render(request,'home.html',{'data':data})
