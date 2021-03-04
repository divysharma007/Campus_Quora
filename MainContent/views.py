from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,Question,Enroll,User,category,comment,profile as user_profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User as User1
from .forms import user_registeration_form,photos,posts
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect,JsonResponse
from django.core.mail import send_mail

#@login_required(login_url='login')
#For searching cateogries
def searchcategory(request):
    if 'term' in request.GET:
        val=str(request.GET.get('term'))
        ca=category.objects.filter(category__icontains=val)
        title=[]
        for term in ca:
            title.append(term.category)
        return JsonResponse(title,safe=False)
    return render(request,'searchcategory.html')    


#Signup 
def register(request):

    form=user_registeration_form()
    if request.method == 'POST':

        form=user_registeration_form(request.POST)
        if form.is_valid():
              
              
              form.save()
              user=User1.objects.all().get(username=request.POST.get('username'))
              user.is_staff=True
              user.save()
              profile=user_profile()
              profile.user=user
              profile.save()

              messages.success(request,f'Account Saved!')
              
              return HttpResponseRedirect('login')
        else :
            return render(request,'register.html',{'form':form}) 
    else :
        return render(request,'register.html',{'form':form})              
#@login_required(login_url='login')
#Profile Page
def profile(request):
    img=request.user.profile.image.url
    img='..'+img
    return render(request,"profile.html",{'user':request.user,'img':img})

#@login_required(login_url='login')
#Shows all the posts related to a particular question.
def anspage(request,id,id3) :
    question=Question.objects.get(pk=id)
    post=question.post.all()
    return render(request,"anspage.html",{"Post":post ,'id':id ,'id3':id3})   
#@login_required(login_url='login')     
#Shows the page which shows a particular post.
def post_page(request,id3,id,id1):
    post=Post.objects.all().filter(pk=id1)
    post=post[0]
    total_likes=post.like.count()
    user=request.user
    return render(request,"post_page.html",{'Post':post,"id1":id1,"id3":id3,"id":id,'total_likes':total_likes,"user":user})

#@login_required(login_url='login')
#Update Profile Picture
def Update_Profile_Photo(request):
    
    if(request.method=='POST'):
      if request.FILES['image']:
        user=request.user
        user.profile.image=request.FILES['image']
        user.profile.save()
        return  redirect('profile')
      else:
        return render(request,"updateprofilephoto.html")    
       
    else:
        return render(request,"updateprofilephoto.html")


#@login_required(login_url='login')
#Shows all the questions related to a particular category.
def Question_Page(request,id3):
    required_category=category.objects.get(pk=id3)
    all_questions=Question.objects.all().filter(category=required_category)
    user=request.user
    return render(request,"Question_page.html",{"all_questions":all_questions,"id3":id3,"user":user})


#For adding answer related to a particular question
def addanswer(request,id,id3):   
     form1=posts() 
     if request.method == 'POST':
        form = request.POST
        if form.get('topic') and form.get('introduction') and form.get('title')  and form.get('post'):
            form = request.POST
            post =Post()
            enroll=Enroll()
            post.topic= form.get('topic')
            post.introduction = form.get('introduction')
            post.title = form.get('title')
            current_user=User1.objects.get(pk=request.user.id)
            current_user=current_user.username
            post.writer=User1.objects.get(username=current_user)
            post.post = form.get('post')
            question=Question.objects.get(pk=id)
            enroll.post=post
            enroll.question=question
            post.save()
            enroll.save()
            
            return  redirect('anspage',id3,id)
        else:
            return render(request,'addans.html',{'form':form1})
     else:
        return render(request,'addans.html',{'form':form1})

#For adding questions related to a particular category
def addques(request,id3):
    if request.method == 'POST':
        form = request.POST
        if form.get('question') :
       
         form = request.POST
         question = Question()
         question.question=form.get('question')
         
         current_category=category.objects.get(pk=id3)
         question.category=current_category
         user=User1.objects.get(pk=request.user.id)
         username=user.username
         question.user=User1.objects.get(username=username)
         question.save()   
         return  redirect('Question_Page',id3) 
        else:
            return render(request,'addques.html')
    else:
        return render(request,'addques.html')
#For editing Answers
def editans(request,id,id1,id3):
    previousanswer =Post.objects.get(pk=id1)
    previousanswer_post =posts(request.POST or None,instance=previousanswer)
    if request.method == 'POST':
         previousanswer_post.save()
         return  redirect('anspage',id3,id)        
        
    else:
        return render(request,'editans.html',{"ans":previousanswer_post})

#For editing a question.
def editques(request,id,id3):
    previousquestion =Question.objects.get(pk=id)
    previousquestion =previousquestion.question
    if request.method == 'POST':
        form = request.POST
        if form.get('newques'):
       
         form = request.POST
         question =Question.objects.get(pk=id)
         question.question=form.get('newques')
         
         question.save()
         
         return  redirect('Question_Page',id3) 
        else:
            return render(request,'editques.html',{"ques":previousquestion})
    else:
        return render(request,'editques.html',{"ques":previousquestion})

#@login_required(login_url='login')
#For deleting a question
def deleteques(request,id,id3):
    question=Question.objects.get(pk=id)
    posts=question.post
    posts=posts.all()
    posts.delete()
    question.delete()
    return  redirect('Question_Page',id3) 

#@login_required(login_url='login')
#For deleting an answer
def deleteans(request,id,id3,id1):
    answer =Post.objects.get(pk=id1)

    answer.delete()
    return  redirect('anspage',id3,id)  

#@login_required(login_url='login')
#For adding comments
def addcomment(request,id,id1,id3):
    if request.method == 'POST':
        form = request.POST
        if form.get('comment'):
         form = request.POST
         new_comment=comment()
         post =Post.objects.get(pk=id1)
         new_comment.post=post
         new_comment.user=User1.objects.get(pk=request.user.id)
         new_comment.body=form.get('comment') 
         new_comment.save()
         return redirect('post_page',id3,id,id1)        
        else:
            return render(request,'addcomment.html')
    else:
        return render(request,'addcomment.html')

#@login_required(login_url='login')
#For liking an answer.
def likeans(request,id,id1,id3):
    
    post=Post.objects.get(pk=id1)
    current_user=User1.objects.get(pk=request.user.id)
    post.like.add(current_user)
    post.save()
    return redirect('post_page',id3,id,id1)
#@login_required(login_url='login')
#It shows all the different categories that are present on the website
def categories(request):
    all_categories=category.objects.all()
    return render(request,"categories.html",{"all_categories":all_categories})

