from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarView.as_view(), name='home'),
    path('search', SearchCar, name='search'),
    path('captcha/', include('captcha.urls')),
]
