import phonenumbers
from phonenumbers import geocoder, carrier, timezone, region_code_for_number
from opencage.geocoder import OpenCageGeocode
from myphone import number

# Parse phone number
pepnumber = phonenumbers.parse(number)

# Validate number
if phonenumbers.is_valid_number(pepnumber):
    # Extract basic details
    state = geocoder.description_for_number(pepnumber, "en")  # e.g., "Karnataka"
    region_code = region_code_for_number(pepnumber)           # e.g., "IN"
    country_name = phonenumbers.region_code_for_country_code(pepnumber.country_code)
    service_provider = carrier.name_for_number(pepnumber, "en")
    time_zones = timezone.time_zones_for_number(pepnumber)

    print(f"State / Region: {state}")
    print(f"Country Code: {region_code}")
    print(f"Country: {country_name}")
    print(f"Carrier: {service_provider}")
    print(f"Time Zone(s): {', '.join(time_zones)}")

    # Now get latitude and longitude via OpenCage
    key = 'cff02359a0cf49a78a5cd5a810ee2fbd'  # Use your actual API key here
    geocoder_api = OpenCageGeocode(key)

    query = f"{state}, {region_code}"
    results = geocoder_api.geocode(query)

    if results and 'geometry' in results[0]:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f" Latitude: {lat}")
        print(f" Longitude: {lng}")
    else:
        print("Could not retrieve coordinates.")
else:
    print("Invalid phone number.")






