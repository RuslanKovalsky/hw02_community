from . import views
from django.urls import path


app_name = 'posts'

urlpatterns = [
    # Это главная страница
    path('', views.index, name="index"),
    # Страница сообществ
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
# group это url адрес который мы забиваем в браузере
