from django.db import models
import os

# Create your models here.

class UploadedFile(models.Model):
    
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    original_name = models.CharField(max_length=255)
    file_size = models.PositiveIntegerField()
    file_extension = models.CharField(max_length=10)


    def save (self, *args, **kwargs):
        
        # Calculate file size and extension
        
        self.original_name = os.path.basename(self.file.name)
        self.file_extension = os.path.splitext(self.file.name)[1].lower()
        self.file_size = self.file.size
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        if self.file:
            self.file.delete(save=False)
        super().delete(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.original_name} ({self.file_size} bytes)"
    