from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', include('main.urls'), name="schooler_home"),
    url(r'^admin/', admin.site.urls),
]

