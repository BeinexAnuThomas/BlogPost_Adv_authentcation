from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('register/',views.register,name='register'),
    path('register_new/',views.Register.as_view(),name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('createBlog/',views.createBlog,name='createBlog'),
    path('viewBlog/',views.viewBlog,name='viewBlog'),
    path('updateBlog/<str:pk>/',views.updateBlog,name='updateBlog'),
    path('deleteBlog/<str:pk>/',views.deleteBlog,name='deleteBlog'),
]
