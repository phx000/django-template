from django.http import JsonResponse
from django.db import connection
from api.tasks import test_task


def error_404(request):
    return JsonResponse({"detail": "This resource does not exist."}, status=404)

def health_check(request):
    return JsonResponse({"status": "ok"})

def readiness_check(request):
    def return_error():
        return JsonResponse({"status": "error"}, status=500)

    try:
        connection.ensure_connection()
    except Exception:
        return return_error()

    try:
        test_task.delay()
    except Exception:
        return return_error()

    return JsonResponse({"status": "ok"})





