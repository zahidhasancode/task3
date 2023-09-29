# author : md zahid hasan 
import googlemaps
api_key = 'API_KEY'

def get_geolocation(address):
    gmaps = googlemaps.Client(key=api_key)
    
    # Geocode the address
    geocode_result = gmaps.geocode(address)
    
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None

if __name__ == '__main__':
    address = input("Enter an address: ")
    result = get_geolocation(address)
    
    if result:
        latitude, longitude = result
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Address not found.")
