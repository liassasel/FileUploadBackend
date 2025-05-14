from rest_framework import serializers
from .models import UploadedFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'uploaded_at', 'original_name', 'file_size', 'file_extension']