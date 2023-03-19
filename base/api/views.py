from django.http import JsonResponse


def getRoutes(request):
    routes = [
        'GET /api/',
        'GET  /api/posts',
        'GET /api/posts/:id',
    ]
    return JsonResponse(routes, safe=False)
