from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from school import urls as school_urls

router = routers.DefaultRouter()
school_urls.register_api_urls(router)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', include('main.urls'), name="schooler_home"),
    url(r'^admin/', admin.site.urls),
]
