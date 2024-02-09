from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('_date_created')
    serializer_class = TaskSerializers


