from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import login_page, home_page, register_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('products/', include('products.urls')),
    path('search/', include('search.urls'))
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


