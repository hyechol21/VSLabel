from django.shortcuts import render
from rest_framework import viewsets
from .models import UploadFile
from .serializers import UploadFileSerializer


class UploadFileView(viewsets.ModelViewSet):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer
     
