
#Vehicle lookup by make - year
import requests

def get_models_for_make_year(make, year):
    """
    Fetch models for a specific make and year using the NHTSA API.
    Returns a list of model names or an empty list on error.
    """
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/{make}/modelyear/{year}?format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return [model['Model_Name'] for model in data.get('Results', [])]
    else:
        print("❌ Error fetching data from NHTSA API")
        return []

def run_vehicle_lookup():
    
    print("🚗 Vehicle Lookup: Find models by make and year")

    make = input("Enter car make (e.g., honda): ").strip().lower()
    year = input("Enter model year (e.g., 2020): ").strip()

    if not year.isdigit() or len(year) != 4:
        print("❌ Invalid year format. Please enter a 4-digit year.")
        return

    models = get_models_for_make_year(make, year)

    if models:
        print(f"\n✅ Models for {make.capitalize()} in {year}:")
        for m in models:
            print(f"- {m}")
    else:
        print(f"❌ No models found for {make} in {year}.")

# Optional standalone run
if __name__ == "__main__":
    run_vehicle_lookup()
