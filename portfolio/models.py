from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

# upload_to = 'images/' 업로드된 이미지들을 images 폴더 안에 넣으라는 의미