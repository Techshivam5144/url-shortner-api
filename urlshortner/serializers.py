from rest_framework import serializers
from .models import ShortUrl

class UrlSerializer(serializers.ModelSerializer):
    shortcode = serializers.CharField(read_only=True)
    class Meta:
        model = ShortUrl
        fields = ["originalurl","shortcode"]

