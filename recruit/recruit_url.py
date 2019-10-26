from django.contrib.auth.decorators import login_required
from django.urls import path

from recruit import views

urlpatterns = [
    path('chat/', login_required(views.recruit_chat), name='contact_with_clients'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('send_message/', views.send_message, name='send_message'),
    path('chat_update/', views.chat_update, name='chat_update'),
    path('check_mes/', views.check_mes, name='check_mes'),
    path('', views.recruit_main_page, name='main_page'),
    path('add_task', views.add_task, name='add_task'),
    path(r'add_new_task',views.add_new_task),
    path(r'favorites/', views.favorites, name='favorites'),
    path(r'checkfavor/', views.check_favor, name='check_favor'),
    path('base/', views.recruit_base, name='recruit_base'),

]