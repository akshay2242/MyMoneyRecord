from django.urls import path
from . import views
urlpatterns = [
    path('create_user/', views.CreateUser.as_view(), name='create_user'),
    path('create_record/', views.CreateRecord.as_view(), name='create_record'),
    path('update_record/<int:pk>/', views.UpdateRecord.as_view(), name='update_record'),

    path('', views.userLogin, name='user_login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_dashboard/', views.UserDashboard.as_view(), name='user_dashboard'),
    path('admin_login/', views.adminLogin, name='admin_login'),
    path('admin_dashboard/', views.AdmindDasboard.as_view(), name='admin_dashboard'), 
]
