from django.db import models
from datetime import date
from django.contrib.auth.models import User as User1
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
class User(models.Model):
    name=models.CharField(max_length=50,default="None")
    password=models.CharField(max_length=50,default="None")
    email=models.CharField(max_length=100 ,default="ABC@gmail.com")
    
    def __str__ (self):
        return self.name


class profile(models.Model):
    user=models.OneToOneField(User1,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(default="IIT_Guwahati_Logo.svg.png",upload_to='profile_pics' )
    def __str__(self):
        return 'Profile'
class Post(models.Model):
    topic = models.CharField(max_length=100,default="nothing")
    post = RichTextUploadingField(blank=True,null=True,config_name='special'
    )
    introduction = models.CharField(max_length=200,default="nothing")
    title=models.CharField(max_length=100,default="nothing")
    writer=models.ForeignKey(User1,on_delete=models.CASCADE,blank=True,null=True)
    like=models.ManyToManyField(User1,related_name="likes")

    def save(self):
        self.slug=slugify(self.title)
        super(Post,self).save()
    def __str__(self):
        return '%s' % self.title    
    
    
    
    def __str__ (self):
        return self.title
class category(models.Model):
    category=models.CharField(max_length=100,default="None")
    def __str__(self):
        return self.category
class Question(models.Model):
       user=models.ForeignKey(User1,on_delete=models.CASCADE,blank=True,null=True)
       category=models.ForeignKey(category,on_delete=models.CASCADE)
       post=models.ManyToManyField(Post, through='Enroll')
       question=models.CharField(max_length=100,default="None")
       
       def __str__(self):
           return self.question

class Enroll(models.Model):
        post=models.ForeignKey(Post,on_delete=models.CASCADE) 
        question=models.ForeignKey(Question,on_delete=models.CASCADE)
        date_join=models.DateField(default=date.today)
class comment(models.Model):
     post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE) 
     user=models.CharField(max_length=50)
     body=models.TextField()
     date_added=models.DateTimeField(auto_now_add=True)
     def __str__(self):
         return '%s -%s' % (self.post.title,self.user)
 



 
