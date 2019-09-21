from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Q, Avg, Min, Max
from django.db.models.functions import ExtractMonth, ExtractWeekDay
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

    ads = AdUnits()
    if request.method == 'POST':
        units = ads.filter_by_date(request)
        avg_units = units.aggregate(Avg('turnover'))
        return JsonResponse({'average_turnover': avg_units['turnover__avg']}, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def avg_chg_high_low(request):
    """
    Returns average change in difference of High and Low
    """

    ads = AdUnits()
    if request.method == 'POST':
        units = ads.filter_by_date(request)
        avg_chg = units.annotate(diff=F('high')-F('low')).aggregate(avg_diff=Avg('diff'))
        return JsonResponse(avg_chg, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def avg_open_close_by_month(request):
    """
    Returns month wise average of open and close
    """

    if request.method == 'GET':
        units = AdUnits.objects.all()
        avg_opn_cls = list(units.annotate(month=ExtractMonth('date')).values('month').annotate(
            open_avg=Avg('open'), close_avg=Avg('close')).values(
                'open_avg', 'close_avg', 'month'))
        return JsonResponse(avg_opn_cls, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def turnover_by_day(request):
    """
    Returns average, minimum and maximum value of turnover by weekday / day name
    """

    ads = AdUnits()
    if request.method == 'GET':
        units = AdUnits.objects.all()
        turnovr_by_wkday = list(units.annotate(weekday=ExtractWeekDay('date')).values(
            'weekday').annotate(
                turnover_avg=Avg('turnover'), turnover_min=Min('turnover'),
                turnover_max=Max('turnover')).values(
                    'turnover_avg', 'turnover_min', 'turnover_max', 'weekday'))
        for idx, wk in enumerate(turnovr_by_wkday):
            turnovr_by_wkday[idx].update({'week_name': ads.WEEK[wk['weekday']]})
        return JsonResponse(turnovr_by_wkday, safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def neg_volatility(request):
    """
    Returns average, minimum and maximum value of turnover by weekday / day name
    """

    ads = AdUnits()
    if request.method == 'GET':
        units = AdUnits.objects.all().filter(Q(open=F('high')))
        neg_volate = units.annotate(diff=F('high')-F('low')).order_by('id')[:10]
        return JsonResponse(list(neg_volate.values()), safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)
