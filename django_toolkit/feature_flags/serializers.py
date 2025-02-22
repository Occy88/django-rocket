from rest_framework import serializers

from django_toolkit.feature_flags.models import FeatureFlag


class FeatureFlagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = FeatureFlag
