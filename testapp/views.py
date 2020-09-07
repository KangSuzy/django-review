from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Blog, Comment
from .form import BlogPost,CommentForm

# Create your views here.
def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해 준다
    # GET 정보를 받아오는 데이터 (딕셔너리 자료형)를 가르킴
    # get 딕셔너리 자료형에서 key 값으로 value를 찾을때 사용
    posts = paginator.get_page(page)

    return render(request,'home.html',{'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
         comment_form = CommentForm(request.POST)
         comment_form.instance.blog_id = pk
         if comment_form.is_valid():
             comment = comment_form.save()
    comment_form = CommentForm()
    comments = blog_detail.comments.all()
    return render(request, 'detail.html', {'blog':blog_detail, 'comments':comments, 'comment_form': comment_form})

# pk 모델의 많은 객체들을 구분하는 구분자
 

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/testapp/'+str(blog.id)) 
    # render와 달리 요청받은 url로 넘김


def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})

def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blog = get_object_or_404(Blog, pk= comment.blog.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/blog/'+str(blog.id))
    else:
        form = CommentForm(instance = comment)
    return render(request, 'blog/comment_update.html', {'form':form})

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blog = get_object_or_404(Blog, pk= comment.blog.id)
    if request.method == 'POST':
        comment.delete()
        return redirect('/blog/'+str(blog.id))
    else:
        form = CommentForm(instance = comment)
    return render(request, 'blog/comment_delete.html', {'object':comment})