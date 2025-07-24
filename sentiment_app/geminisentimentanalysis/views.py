from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from sentiment_app.prompts import Prompts
import json
# Create your views here.
from geminisentimentanalysis.generate_response import GenerateResponse

# declare an object

response=GenerateResponse()

class GeminiSentiment(APIView):
    prompttype=None
    def post(self,request):
        try:
            if request.method !='POST':
                return Response({'result':{},'status':"Failure",'message':'Get request not allowed'}, status = 400)
            
            user_review=request.data.get('userReview')
            prompt = self.prompttype(user_review)
            rawresponse=response.getresponse(prompt)

            cleaned = rawresponse.replace("```json", "").replace("```", "").strip()
            classification = json.loads(cleaned)

            return Response({"Response": classification, "status": "Success"})
        except Exception as e:
            return Response({"status": "Failure", "message : ": str(e)}, status=400)

class ZeroShot(GeminiSentiment):
    prompttype = Prompts().ZeroShot

class FewShots(GeminiSentiment):
    prompttype = Prompts().FewShots

class ChainOfThought(GeminiSentiment):
    prompttype = Prompts().ChainOfThought