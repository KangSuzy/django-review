from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog # models.py 정의된 blog class 와 연결
        fields = ['title', 'body'] #입력받길 원하는 속성

# views.py 직접 적어도 되지만 forms.py 를 사용하는 이유
# 효율적인 코드 관리를 위해 import 해서 사용함