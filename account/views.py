from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializers import UserSerializer, VerifyAccountSerializer
from .emails import send_otp_via_email
from .models import User
# Create your views here.
class RegisterAPI(APIView):
    def post(self,request):
        try:
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({'msg':'Registration Successful'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            print(e)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
class VerifyOTP(APIView):
    def post(self,request):
        try:
            serializer=VerifyAccountSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                email=serializer.data['email']
                otp=serializer.data['otp']
                user= User.objects.filter(email=email)
                if not user.exists():
                    return Response({'data':'Invalid email'},{'msg':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
                if user[0].otp!=otp:
                    return Response({'data':'Wrong otp'},{'msg':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
                user=user.first()
                user.is_verified=True
                user.save()
                return Response({'msg':'Account verified','data':serializer.data},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            print(e)  
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)       