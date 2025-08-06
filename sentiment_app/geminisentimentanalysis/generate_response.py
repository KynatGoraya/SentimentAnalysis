

#-----------------------GEMINI------------------------------
import os
import google.generativeai as gen
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
# api_key = os.getenv("OPENAI_API_KEY")
#print(api_key)
try:
    gen.configure(api_key=api_key)
except Exception as e:
    print(" Key is Invalid, gen config not work")

class GenerateResponse:
    def __init__(self, model_name="gemini-2.5-flash"):
        try:
            self.model = gen.GenerativeModel(model_name)
        except Exception as e:
            print("Model not loading:", e)
            
    def getresponse(self, prompt):
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.6
                }
            )
            print(response.text)
            return response.text
        except Exception as e:
            return f"Error in generating response:{e}"



#-------------------------------OPENAI---------------------------------
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     raise ValueError("OPENAI_API_KEY not found in .env file")

# client = OpenAI(api_key=api_key)

# class GenerateResponse:
#     def __init__(self, model_name="gpt-4.1-mini"):
#         self.model_name = model_name

#     def getresponse(self, prompt):
#         try:
#             response = client.chat.completions.create(
#                 model=self.model_name,
#                 messages=[
#                     {"role": "system", "content": "You are a helpful medical assistant."},
#                     {"role": "user", "content": prompt}
#                 ],
#                 temperature=0.6
#             )
#             return response.choices[0].message.content.strip()
#         except Exception as e:
#             return f"Error in generating response: {e}"
