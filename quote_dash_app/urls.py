from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index),
    path('addUser', views.addUser),
    path('dashboard', views.dashboard),
    path('login', views.login),
    path('logout', views.logout),
    path('create_quote',views.create_quote),
    path('delete_quote/<int:quote_id>', views.delete_quote),
    path('edit_user', views.edit_user),
    path('update_user', views.update_user),
    path('show_user/<int:user_id>', views.show_user),
    path('like/<int:quote_id>/<int:user_id>', views.like),
]