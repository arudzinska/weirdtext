from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import encode, decode
from .exceptions import NotEncoderFormatError


class Encode(APIView):
    """
    Text encoding APIView.
    """
    
    def post(self, request):
        try:
            response = Response(encode(r'{}'.format(request.data['text'])))
        except MultiValueDictKeyError:
            response = Response("ERROR: key 'text' is required in the body", status=status.HTTP_400_BAD_REQUEST)
        return response


class Decode(APIView):
    """
    Text decoding APIView.
    """
    
    def post(self, request):
        try:
            response = Response(decode('{}'.format(request.data['text'])))
        except NotEncoderFormatError:
            response = Response("ERROR: String doesn't have a proper Encoder output format",
                                status=status.HTTP_400_BAD_REQUEST)
        except MultiValueDictKeyError:
            response = Response("ERROR: key 'text' is required in the body", status=status.HTTP_400_BAD_REQUEST)
        return response
