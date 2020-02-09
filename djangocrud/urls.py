from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]