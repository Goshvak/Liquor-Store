from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('review/', views.review_view, name = 'review'),
    path('products/', views.products, name='products' ),
]
