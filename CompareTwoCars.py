#compare two cars
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found. Please set it in your .env file.")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def gemini_prompt(make1, model1, make2, model2):
    return (
        f"Compare the following two cars:\n"
        f"1. {make1} {model1}\n"
        f"2. {make2} {model2}\n\n"
        f"Include details about:\n"
        f"- Performance\n"
        f"- Reliability\n"
        f"- Common issues\n"
        f"- Fuel economy\n"
        f"- Safety\n"
        f"- Buying advice\n"
        f"Make it suitable for someone choosing between the two cars."
    )

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error while calling Gemini API: {e}"

def run_car_comparison():
    print("🚗 Enter details of the first car:")
    make1 = input("Car Brand Name (e.g., BMW): ").strip()
    model1 = input("Car Model (e.g., M5): ").strip()

    print("\n🚙 Enter details of the second car:")
    make2 = input("Car Brand Name (e.g., Toyota): ").strip()
    model2 = input("Car Model (e.g., Camry): ").strip()

    prompt = gemini_prompt(make1, model1, make2, model2)
    print("\n🔍 Please wait...\n")
    answer = ask_gemini(prompt)

    print("📋 Result:\n")
    print(answer)

if __name__ == "__main__":
    run_car_comparison()
