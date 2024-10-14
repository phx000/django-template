from api.drf import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^.*$', views.error_404_view, name="404"),
]
