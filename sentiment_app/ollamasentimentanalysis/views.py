# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .generate_response import GenerateResponse
from sentiment_app.prompts import Prompts
import json

generator = GenerateResponse()


class OllamaSentiment(APIView):
    prompttype=None

    def post(self, request):
        try:
            user_review = request.data.get("userReview")
            if not user_review:
                return Response({"status": "Failure", "message": "Missing user review"}, status=400)

            prompt = self.prompttype(user_review)
            rawresponse = generator.getresponse(prompt)
            cleaned = rawresponse.replace("```json", "").replace("```", "").strip()
            classification = json.loads(cleaned)

            return Response({"Response": classification, "status": "Success"})
        except Exception as e:
            return Response({"status": "Failure", "message : ": str(e)}, status=400)
    
class ZeroShot(OllamaSentiment):
    prompttype = Prompts().ZeroShot

class FewShots(OllamaSentiment):
    prompttype = Prompts().FewShots

