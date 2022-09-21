from . import views
from django.urls import path


app_name = 'posts'

urlpatterns = [
    # Это главная страница
    path('', views.index, name="index"),
    # Страница сообществ
    # path('group_list/', views.group_list, name='group_list'),
    path('group_list/<slug:pk>/', views.group_list, name='group_list'),
]
