from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    # Dashboard / Tasks
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:srno>/', views.toggle_task, name='toggle_task'),
    path('edit/<int:srno>/', views.edit_task, name='edit_task'),
    path('delete/<int:srno>/', views.delete_task, name='delete_task'),
]
