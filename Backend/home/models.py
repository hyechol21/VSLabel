from django.db import models

class UploadFile(models.Model):
    # file = models.FileField()
    # uploaded_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    
    # def __str__(self):
    #     return self.uploaded_on.date()
    
    
    
