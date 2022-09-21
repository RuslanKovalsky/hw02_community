from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    # path('group/', include('posts.urls', namespace='group_list')),
    # path('admin/', admin.site.urls),
]
