from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Donation

from donation import serializers

class DonationViewSet(viewsets.ModelViewSet):
    """Manage donation in the database"""
    serializer_class = serializers.DonationSerializer
    queryset = Donation.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the donations for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new donation"""
        serializer.save(user=self.request.user)
