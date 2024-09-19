from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import ColaboradorViewSet
from rest_framework.authtoken import views 

router = routers.DefaultRouter()
router.register(r'colaboradores', ColaboradorViewSet, basename='colaborador')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'), 
    path('admin/', admin.site.urls),
]
