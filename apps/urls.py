from django.urls import include, path
from django.contrib import admin
from theme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('eventos_cbv/', include('eventos_cbv.urls', namespace='eventos_cbv')),
    path('', views.home),
    # path('', include('pages.urls')),
]
