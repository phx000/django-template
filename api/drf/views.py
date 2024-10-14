from django.http import JsonResponse


def error_404_view(request):
    return JsonResponse({
        "detail": "This resource does not exist."
    }, status=404)
