from rest_framework import viewsets
from .models import leads
from leads.serializers import LeadsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LeadsViewSet(viewsets.ModelViewSet):
    queryset=leads.objects.all()
    serializer_class=LeadsSerializer
    permission_classes=[IsAuthenticated]

