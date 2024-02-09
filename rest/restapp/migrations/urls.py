from django.urls import include, url  # Update the import statement
from django.contrib import admin
from rest_framework import routers
from rest.app.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),  # Update the usage of url
    url(r'admin/', admin.site.urls),
    ]
