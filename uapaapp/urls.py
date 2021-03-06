from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from school import urls as school_urls


router = routers.DefaultRouter()
school_urls.register_api_urls(router)

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^$', include('main.urls'), name="schooler_home"),
    url(r'^school/', include('school.urls')),
    url(r'^admin/', admin.site.urls),

]
