from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from files.models import UploadedFile
from django.http import FileResponse

# Create your views here.

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    
    def post(self, request):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        
        uploaded_file = UploadedFile(file=file_obj)
        uploaded_file.save()
        
        serializer = FileSerializer(uploaded_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class FileListView(APIView):
    def get(self, request):
        files = UploadedFile.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
    
class FileDownloadView(APIView):
    def get(self, request, file_id):
        try:
            uploaded_file = UploadedFile.objects.get(id=file_id)
            return FileResponse(uploaded_file.file.open(), filename=uploaded_file.original_name)
        except UploadedFile.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        
class FileDeleteView(APIView):
    def delete(self, request, file_id):
        try:
            file = UploadedFile.objects.get(id=file_id)
            
            file.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        except UploadedFile.DoesNotExist:
            return Response(
                {"error": "File not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )