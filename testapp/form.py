from django import forms
from .models import Blog, Comment

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog # models.py 정의된 blog class 와 연결
        fields = ['title', 'body'] #입력받길 원하는 속성
class CommentForm(forms.ModelForm):
    body =  forms.CharField(label='댓글', widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['body']

# views.py 직접 적어도 되지만 forms.py 를 사용하는 이유
# 효율적인 코드 관리를 위해 import 해서 사용함