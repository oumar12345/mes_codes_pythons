import phonenumbers
from myphone import number
from phonenumbers import geocoder
import folium

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "fr")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "fr"))

from opencage.geocoder import OpenCageGeocode

key  = 'a8a114d777024a0b9faf414da7adf582'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
if results:
    lat = results[0]["geometry"]["lat"]
    lng = results[0]["geometry"]["lng"]

    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    myMap.save("Mylocation.html")
else : 
    print("No results found")


#########################################################
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
location_geopy = geolocator.geocode(location)

if location_geopy:
    print("Geopy Location:", location_geopy.address)
    print("Latitude:", location_geopy.latitude, "Longitude:", location_geopy.longitude)
    # Add marker from geopy results
    folium.Marker([location_geopy.latitude, location_geopy.longitude], popup=location_geopy.address).add_to(myMap)
    # Save the updated map
    myMap.save("Mylocation_updated.html")
else:
    print("No results found for the location using Geopy.")