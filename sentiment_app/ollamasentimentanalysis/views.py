# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .generate_response import GenerateResponse

generator = GenerateResponse()

class OllamaSentiment(APIView):
    def post(self, request):
        try:
            user_review = request.data.get("userReview")
            if not user_review:
                return Response({"status": "Failure", "message": "Missing user review"}, status=400)

            prompt = f"Classify the sentiment of this review as Positive, Negative, or Neutral:\n{user_review}"
            classification = generator.getresponse(prompt)
            return Response({'status':"Success","Response":{classification}})
        except Exception as e:
            return Response({"status": "Failure", "message : ": str(e)}, status=400)
