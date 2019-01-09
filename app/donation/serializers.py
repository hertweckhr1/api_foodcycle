from rest_framework import serializers
from core.models import Donation

class DonationSerializer(serializers.ModelSerializer):
    """Serialize a donation"""

    class Meta:
        model = Donation
        fields = (
            'id', 'user', 'product_type', 'product_description', 'product_measurement',
            'quantity', 'pickup_details', 'pickup_starttime', 'pickup_endtime',
            'donee'
        )
        read_only_fields = ('id',)
