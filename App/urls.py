from django.urls import path
from .views import HomePageview, AboutPageview

urlpatterns = [
    path ('', HomePageview.as_view(), name='home'),
    path ('about/', AboutPageview.as_view(), name='about')

]