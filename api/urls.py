from django.urls import re_path, path
from django.http import JsonResponse

from api.views.functional_views import error_404, health_check, readiness_check

urlpatterns = [
    path("healthz", health_check, name="healthz"),
    path("readiness", readiness_check, name="readiness"),
    re_path(r'^.*$', error_404, name="404"),
]
