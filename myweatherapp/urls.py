from django.contrib import admin
from django.urls import path, include
from myweatherappapi.urls import urlpatterns as api_urls
from frontend.urls import urlpatterns as frontend_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
    path('', include(frontend_urls))
]
