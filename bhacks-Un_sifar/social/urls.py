from django.urls import path,include
from . import views
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.index,name='index'),
    path('profile/', views.profile,name='profile'),
    path('update/', views.update,name='update'),
    path('chat/',views.chatroom,name='chat'),
    path('courses/add/',views.adding,name='add'),
    path('courses/<pk>/',views.lecture,name='lecture'),
    path('courses/<user_id>/lecture/<pk>/add/',views.add_lecture,name='add-lecture'),
    path('reply/<pk>/',views.reply_fun,name='reply'),
    path('courses/', views.show,name='courses'),
    path('subscribe/<pk>/', views.subscribe,name='subscribe'),
    path('profile/edit/', views.profile_change,name='profile_change'),
    path('password/change/', views.ChangePassword,name='ChangePassword'),
    path('password/reset/', PasswordResetView.as_view(),{'template_name':'registration/password_reset_form.html'},name='password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('send/',views.send,name='send'),
    path('about/',views.about,name='about'),

]