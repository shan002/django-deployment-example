from django.urls import path
from blog_app import views


app_name = 'blog_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newpost/', views.new_post, name='new_post'),
    path('signup/', views.sign_up, name='sign_up'),
    path('', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout')
]
