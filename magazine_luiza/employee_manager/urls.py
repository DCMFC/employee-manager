from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('api.urls')),
    url(r'^api-token/', views.obtain_auth_token)
]
