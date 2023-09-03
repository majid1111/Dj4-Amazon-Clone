from django.urls import path
from.views import Productlist , ProductDetail



urlpatterns = [
    path('',Productlist.as_view()),
    path('<slug:slug>/' ,ProductDetail.as_view()),


]