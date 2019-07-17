from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Product

# Create your views here.


class ProductFeaturedListView(ListView):
    queryset = Product.objects.featured()
    template_name = 'products/product_list.html'


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/product_featured_detail.html'


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'home.html'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = Product.objects.get(slug=slug)
        if instance is None:
            raise Http404('Product not found')
        return instance



