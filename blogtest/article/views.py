from django.shortcuts import render,render_to_response
from article.models import Article,Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import Http404
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from article.forms import BlogForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def home(request):
    post=Article.objects.all()[::-1]
    paginator=Paginator(post,6)
    page=request.GET.get('page')
    try:
        post_article=paginator.page(page)
    except PageNotAnInteger:
        post_article=paginator.page(1)
    except EmptyPage:
        post_article=paginator.page(paginator.num_pages)
    return render(request,'home.html',{'post':post_article})
    

@csrf_exempt     
def write(request):
    errors=[]
    if request.method=='POST':
        title=request.POST['title']
        category=request.POST['category']
        content=request.POST['body']
        
        if len(title)>0 and len(category)>0 and len(content)>0 and request.user.is_authenticated():
            editor=request.user.username
            new=Article.objects.create(title=title,category=category,content=content,editor=editor)
            new.save()
            return HttpResponseRedirect('/')
            
        else:
            errors.append('write again or login')
            return render(request,'write.html',{'errors':errors})
    return render(request,'write.html',{'errors':errors})
            
 
@csrf_exempt           
def login(request):
    errors=[]
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect('/')
        else:
            errors.append('wrong username and password')
            return render(request,'login.html',{'errors':errors})
    return render(request,'login.html',{'errors':errors})
     

def logout(request):
    auth_logout(request)
    return HttpResponse('<a href="/">logouted</a>')
    
def register(request):
    errors=[]
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            if ' ' in username:
                errors.append('no space!')
            else:
                new_user=User.objects.create_user(username=username,password=password)  
                new_user.save()
                return HttpResponseRedirect('/registered/')
        else:
            errors.append('username is exited')
    return render(request,'register.html',{'errors':errors})
        


def post(request,id):
    try:
        post=Article.objects.get(id=str(id))
        comment=post.comment_set.all()[::-1]
    except Article.DoesNotExist:
        raise Http404
    if request.method=='POST':
        newcommentator=request.user.username
        newcomment=request.POST['comment']
        link=Article.objects.get(id=str(id))
        if len(newcomment)>0:
            new=Comment.objects.create(commentator=newcommentator,comment=newcomment,link=link)
            new.save()
        return HttpResponseRedirect('/post/%s/'%id)
    return render(request,'post.html',{'post':post,'comment':comment,})
    
def category_search(request,category):
    try:
        Article.objects.filter(category__exact=category)
    except Article.DoesNotExist:
        return HttpResponse('nothing')
    else:
        article=Article.objects.filter(category__exact=category)
        return render(request,'category.html',{'article':article})

def usershow(request,username):
    try:
        Article.objects.filter(editor__exact=username)
    except Article.DoesNotExist:
        return HttpReponse('he did not write any thing')
    else:
        article=Article.objects.filter(editor__exact=username)
        return render(request,'usershow.html',{'article':article})
        
def formcheck(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            pass
    else:
        form=BlogForm()
    return render(request,'formcheck.html',{'form':form})
    
        
def logined(request):
    return HttpResponse('<a href="/">logined</a>') 
 
def posted(request):
    return HttpResponse('<a href="/">posted</a>')           
            
def commented(request):
    return HttpResponse('<a href="/">commented!</a>')
def registered(request):
    return HttpResponse('<a href="/">registered!</a>')    
