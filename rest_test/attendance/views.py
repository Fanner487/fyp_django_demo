# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


from rest_framework import viewsets
from rest_framework import permissions
from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer
# Create your views here.

class AttendanceViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
