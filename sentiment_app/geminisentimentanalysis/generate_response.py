import os
import google.generativeai as gen
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
#print(api_key)
try:
    gen.configure(api_key="api_key")
except Exception as e:
    print(" Key is Invalid, gen congif not work")

class GenerateResponse:
    def __init__(self):
        try:
            self.model=gen.GenerativeModel("gemini-1.5-flash")
        except:
            return "Model not Loading"
    
class GenerateResponse:
    def __init__(self):
        try:
            self.model = gen.GenerativeModel("gemini-1.5-flash")
        except Exception as e:
            print("Model not loading:", e)

    def getresponse(self, prompt):
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.6
            }
        )
        print(response.text)
        return response.text

        
    
