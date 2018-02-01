from django.urls import path, include
from django.contrib import admin

from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('articles.urls')),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]
