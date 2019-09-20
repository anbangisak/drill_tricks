from rest_framework import serializers

from steel.models import AdUnits

class AdUnitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdUnits
        fields = ('id', 'date', 'open', 'close', 'high', 'low', 'turnover', 'share_traded')
