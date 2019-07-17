
from django.views.generic import ListView

from products.models import Product

# Create your views here.


class SearchProductListView(ListView):

    template_name = 'home.html'

    def get_queryset(self):
        print(Product.objects.featured())
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.featured()

