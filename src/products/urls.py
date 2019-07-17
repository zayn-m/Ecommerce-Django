from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    ProductFeaturedListView,
    ProductFeaturedDetailView
    )

app_name = 'products'

urlpatterns = [
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<pk>/', ProductFeaturedDetailView.as_view()),
    path('', ProductListView.as_view(), name='list'),
    path('<slug>/', ProductDetailView.as_view(), name='detail'),
]

