#decode vin
import requests  

def is_valid_vin(vin):
    """
    Check if the provided VIN is valid:
    - Must be exactly 17 characters
    - Must be alphanumeric (letters and numbers only)
    """
    return len(vin) == 17 and vin.isalnum()

def decode_vin(vin):
    """
    Call the NHTSA vPIC API to decode the VIN.
    Uses the DecodeVinValuesExtended endpoint to get detailed info.
    Returns the JSON response as a Python dictionary.
    """
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValuesExtended/{vin}?format=json"
    response = requests.get(url)
    return response.json()

def extract_vehicle_info(results):
    """
    Extract selected vehicle details from the API results.
    The 'results' parameter is a list with a single dictionary containing vehicle info.
    We pull specific keys and return them in a new dictionary.
    If a key is missing, return 'Not Available' for that field.
    """
    keys = ['Make', 'Model', 'ModelYear', 'EngineModel', 'BodyClass', 'FuelTypePrimary']
    vehicle_info = {}

    if not results: 
        return vehicle_info

    item = results[0]  

    for key in keys:
        vehicle_info[key] = item.get(key, 'Not Available')  

    return vehicle_info

def display_vehicle_info(info):
    """
    Nicely print the vehicle information dictionary.
    """
    print("\n🚗 Vehicle Information:")
    for key, value in info.items():
        print(f"{key}: {value}")

def run_vin_decoder():
    """
    Main function to run the VIN decoder:
    - Prompts user for input VIN
    - Validates the VIN format
    - Calls the decode API
    - Extracts and displays vehicle info
    """
    vin = input("Enter your 17-character VIN: ").strip().upper() 

    if not is_valid_vin(vin):
        print("❌ Invalid VIN. Must be 17 alphanumeric characters.")
        return

    print("🔍 Decoding VIN...")
    decoded = decode_vin(vin)
    info = extract_vehicle_info(decoded.get('Results', []))  
    display_vehicle_info(info)

if __name__ == "__main__":
    run_vin_decoder()
