from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from boxe.api import api as boxe_api

urlpatterns = [
    path('', RedirectView.as_view(url='/portfolio/', permanent=False)),
    path("admin/", admin.site.urls),
    path("escola/", include("escola.urls")),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
    path('artigos/', include('artigos.urls')),
    path('boxe/api/', boxe_api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
