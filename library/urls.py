from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^librarian/', include('librarian.urls')),
    #url(r'^Books/', include('librarian.urls')),
    url(r'^$', include('librarian.urls')),
]
