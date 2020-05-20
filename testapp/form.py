from djnago import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog #blog 와 연결
        fields = ['title', 'body'] #입력받길 원하는 속성