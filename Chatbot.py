from VINdecoder import run_vin_decoder
from CompareTwoCars import run_car_comparison
from CarBuying import run_buying_advice
from VehicleLookup import run_vehicle_lookup
from vin_explainer_rag.main import run_vin_info_rag

def main():
    while True:
        print("\n👋 Hello! How can I help you today?")
        print("1 - Decode a VIN")
        print("2 - Compare two cars")
        print("3 - Car buying advice")
        print("4 - Vehicle lookup")
        print("5 - Info about VIN")
        print("0 - Exit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            run_vin_decoder()
        elif choice == '2':
            run_car_comparison()
        elif choice == '3':
            run_buying_advice()
        elif choice == '4':
            run_vehicle_lookup()
        elif choice == '5':
            run_vin_info_rag()
        elif choice == '0':
            print("👋 Goodbye! Have a great day!")
            break
        else:
            print("❌ Invalid option. Please choose a number from the menu.")

if __name__ == "__main__":
    main()
