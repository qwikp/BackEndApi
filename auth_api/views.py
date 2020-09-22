from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView

from . sms_integration import send_sms
from . utils import random_with_N_digits, bd_number_match, swedish_phone_no_formatter


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_registration_token(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password1 = request.data.get("password1")
    password2 = request.data.get("password2")
    if password1 != password2:
        return Response({'error': 'password dont match'},
                        status=HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, email=email, password=password1)
    if not user:
        return Response({'error': 'User can not be created'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        data = {
            'response' : "user log outed"
        }
        return Response(data, status=HTTP_200_OK)


class SendSMS(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, format=None):
        # simply delete the token to force a login
        phone_number = request.data.get("phone")

        # phone number validation to do

        if not bd_number_match(phone_number):
            return Response({'error': 'Invalid phone number'},
                        status=HTTP_400_BAD_REQUEST)

        verification_code = random_with_N_digits(4)
        message = f"your verification code is {verification_code}"

        send_sms(phone_no=swedish_phone_no_formatter(phone_number), message=message)

        data = {
            'response' : "success"
        }
        return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)