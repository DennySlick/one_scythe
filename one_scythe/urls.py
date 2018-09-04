from django.conf.urls import url, include
from django.contrib import admin
#from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('calculator.urls')),
    url(r'^$', main_views.homepage, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
