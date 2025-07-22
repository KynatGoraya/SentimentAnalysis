from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from geminisentimentanalysis.generate_response import GenerateResponse

# declare an object

response=GenerateResponse()

class geminisentiment(APIView):
    def post(self,request):
        try:
            if request.method !='POST':
                return Response({'result':{},'status':"Failure",'message':'Get request not allowed'}, status = 400)
            
            user_review=request.data.get('userReview')
            prompt="Classify the review into positive, negative or neutral. The user review is as follows: {user_review}"
            classification=response.getresponse(prompt)
            return Response({"Response":{classification}, 'status':"Success"})
        except Exception as e:
            return Response({"status": "Failure", "message : ": str(e)}, status=400)

