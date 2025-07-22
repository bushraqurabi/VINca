# Buying Car Advice Script

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found. Please set it in your .env file.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

questions = [
    "What will you mainly use the car for? (e.g., commuting, off-roading, racing, family trips)",
    "What kind of driving do you enjoy most? (e.g., smooth city rides, sporty drifting, rugged terrain, desert driving)",
    "How much money are you willing to spend on your car?",
    "Do you have a preference for the car’s drivetrain? (e.g., front-wheel drive, rear-wheel drive, 4x4)",
    "What best describes your lifestyle? (e.g., urban, outdoorsy, business professional, family-oriented)",
    "What size car do you want? (e.g., compact, sedan, SUV, truck)",
    "Would you consider cars that run on alternative fuels like electric, hybrid, or diesel?",
    "Are you okay if your car uses a lot of fuel, or do you prefer one with moderate or low fuel consumption?"
]

def ask_user_questions():
    print("Please answer the following questions to get personalized car buying advice:\n")
    answers = {}
    for question in questions:
        answer = input(question + " ").strip()
        answers[question] = answer
    return answers

def build_prompt(answers):
    prompt = (
        "You are an expert car buying advisor.\n"
        "Based on the following user preferences, provide detailed buying advice:\n\n"
    )
    for question, answer in answers.items():
        prompt += f"- {question} Answer: {answer}\n"
    prompt += "\nGive recommendations about car types, brands, and features that suit these preferences best."
    return prompt

def get_buying_advice(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error while calling Gemini API: {e}"

def run_buying_advice():
    answers = ask_user_questions()
    prompt = build_prompt(answers)
    print("\nGenerating your personalized car buying advice...\n")
    advice = get_buying_advice(prompt)
    print("📋 Here is your car buying advice:\n")
    print(advice)

if __name__ == "__main__":
    run_buying_advice()
