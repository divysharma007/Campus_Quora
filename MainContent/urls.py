from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.conf.urls import include,url
from django.contrib.auth import views as auth
from django.urls import path
from . import views
urlpatterns = [
    
    path('password_reset_request', auth.PasswordResetView.as_view(template_name='password/password_reset_form.html'),
         name='password_reset_request'),
    path('password_reset/done/', auth.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),

   
     url(r'^searchcategory',views.searchcategory,name='searchcategory'), 
 
     url(r'^profile/$',views.profile,name="profile"),
     url(r'^profile/updateprofilephoto/$',views.Update_Profile_Photo,name="updateprofilephoto"),

     url(r'^register',views.register,name="register"),
     
    
     url(r'^category$',views.categories,name="categories"),
     
     url(r'^category/(?P<id3>[0-9]+)/addques/$',views.addques,name="add_ques"),
     url(r'^category/(?P<id3>[0-9]+)/ans/(?P<id>[0-9]+)/addans/$',views.addanswer,name="add_ans"),
        
     url(r'^category/(?P<id3>[0-9]+)/(?P<id>[0-9]+)/edit/$',views.editques,name="edit_ques"),
     url(r'^category/(?P<id3>[0-9]+)/ans/(?P<id>[0-9]+)/reply/(?P<id1>[0-9]+)/edit/$',views.editans,name="edit_ans"),
     
     url(r'^category/(?P<id3>[0-9]+)/(?P<id>[0-9]+)/delete/$',views.deleteques,name="delete_ques"),
     url(r'^category/(?P<id3>[0-9]+)/ans/(?P<id>[0-9]+)/reply/(?P<id1>[0-9]+)/delete/$',views.deleteans,name="delete_ans"),
     
     url(r'^category/(?P<id3>[0-9]+)/ans/(?P<id>[0-9]+)/$',views.anspage,name="anspage"),
     url(r'^category/(?P<id3>[0-9]+)/ans/(?P<id>[0-9]+)/reply/(?P<id1>[0-9]+)/$',views.post_page,name="post_page"),
     url(r'^category/(?P<id3>[0-9]+)/$',views.Question_Page,name="Question_Page"),

     url(r'^category/(?P<id3>[0-9]+)/ans/(?P<id>[0-9]+)/reply/(?P<id1>[0-9]+)/addcomment/$',views.addcomment,name="comment"),
     url(r'^category/(?P<id3>[0-9]+)/ans/(?P<id>[0-9]+)/reply/(?P<id1>[0-9]+)/like/$',views.likeans,name="like_ans"),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
