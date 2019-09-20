from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from steel.models import AdUnits
from steel.serializers import AdUnitsSerializer
# Create your views here.

@csrf_exempt
def fetch_all(request):
    """
    List all trading details
    """

    if request.method == 'GET':
        units = AdUnits.objects.all()
        serializer = AdUnitsSerializer(units, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse("welcome")
