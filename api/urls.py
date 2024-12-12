from django.urls import re_path
from django.http import JsonResponse


def error_404_view(request):
    return JsonResponse({
        "detail": "This resource does not exist."
    }, status=404)

urlpatterns = [
    re_path(r'^.*$', error_404_view, name="404"),
]
