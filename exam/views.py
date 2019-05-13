from django.http import Http404
from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import auth
from django.contrib.auth.models import User
import re
from .models import *
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser,JSONParser, MultiPartParser, FormParser
from rest_framework import status

def index(request):
    context = {
        'message': 'Hello World!',
    }
    return render(request, 'exam/index.html', context)

class AlbumView(APIView):
    def get(self, request, format=None):
        file = open('logger.txt', 'r')
        contents = file.read()
        file.close()
        file = open('logger.txt', "w")
        file.write(contents + '\nrequest')
        file.close()
        if 'jsonp' in request.GET: 
            return HttpResponse(f'{request.GET["jsonp"]}({Album.get_all()});' , status=status.HTTP_200_OK)
        response = Response(Album.get_all(), status=status.HTTP_200_OK)
        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "*"
        return response
