from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    # admin page title 표시

    def summary(self):
        return self.body[:100]
    # class body 100글자만 출력


# model 작성 후 migration
# $python manage.py makemigrations migration 만들기
# $python manage.py migrate 데이터베이스 적용하기

# model 속성 > admin 양식 결정

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name='comments')
    date = models.DateField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.body