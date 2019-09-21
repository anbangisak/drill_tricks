from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from rest_framework import status
from rest_framework.response import Response

from steel.models import AdUnits
from steel.serializers import AdUnitsSerializer

import datetime


@csrf_exempt
def fetch_all(request):
    """
    List all trading details
    """

    if request.method == 'GET':
        units = AdUnits.objects.all()
        serializer = AdUnitsSerializer(units, many=True)
        return JsonResponse(serializer.data, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_units_adv(request):
    """
    Filters opening price greater than closing price
    """

    if request.method == 'POST':
        print(request.POST)
        strt_dt = datetime.datetime.strptime(request.POST['start'], '%d/%m/%Y')
        end_dt = datetime.datetime.strptime(request.POST['end'], '%d/%m/%Y')
        units = AdUnits.objects.filter(date__range=[strt_dt, end_dt]).filter(open__gte=F('close'))
        serializer = AdUnitsSerializer(units, many=True)
        return JsonResponse(serializer.data, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def avg_turn_over(request):
    """
    Fetches Average Turn over between date range
    """

    pass
