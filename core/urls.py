from django.urls import include, path

from .views import market 

urlpatterns = [
    path('', market.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]