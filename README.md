# VINca – Smart Vehicle Assistant (Chatbot)


VINca is a console-based chatbot that helps users with vehicle information by decoding VINs, offering error code help, comparing cars, giving buying advice, looking up vehicles by make/model/year, and explaining VIN basics. It uses the NHTSA vPIC API and generative AI (Google Gemini API).

---

## Features

1. Decode a VIN
Decode a 17-character VIN and display vehicle details and recall information.
Powered by: NHTSA vPIC API

2. Compare Two or More Cars
Compare the specifications of two vehicles using VINs or make/model/year input.
Powered by: NHTSA vPIC API + Google Gemini AI

3. Car Buying Advice
Get AI-generated, personalized recommendations for buying a vehicle.
Powered by: Google Gemini AI

4. Vehicle Lookup by Make/Model/Year
Lookup available vehicle models by selecting a make and year.
Powered by: NHTSA vPIC API

5. Info about VIN (Educational)
Learn how VINs work, how to read them, and where to find them on a vehicle.
Powered by: RAG + Google Gemini AI

6. Exit
Exit the chatbot interface cleanly.
No external service required

---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/VINca.git
cd VINca

### 2. Create & activate a virtual environment
python -m venv env
env\Scripts\activate   # Windows
source env/bin/activate  # Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Obtain API Keys and Credentials
* Google Gemini API Key
- Go to: https://aistudio.google.com/app/apikey
- Sign in with your Google account.
- Click “Create API Key”.
- Copy the generated key.

* Google Cloud JSON Key
- Go to: https://console.cloud.google.com
- Create a Service Account and download the JSON key file.
- Put the .json file anywhere on your machine.
- Set the environment variable in your .env file or your system:
  Add this line to your .env:
  GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json



### 5. Configure your environment variables
Create a .env file in the project root and add your API keys:
GEMINI_API_KEY=your_google_gemini_api_key_here

### Run the chatbot main script:
python Chatbot.py
