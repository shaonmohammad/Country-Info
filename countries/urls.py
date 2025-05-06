from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CountryViewSet,country_list_view,country_detail

router = DefaultRouter()
router.register('countries', CountryViewSet)

urlpatterns = [
    path('api/  ', include(router.urls)),
    path('web/countries/', country_list_view, name='web-country-list'),
    path('web/country/<int:pk>/', country_detail, name='country_detail'),
]
