from attendance.models import Attendance
from rest_framework import serializers

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = ('event_name', 'created', 'organiser', 'scheduled')
