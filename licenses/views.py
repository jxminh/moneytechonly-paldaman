from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models


def all_licenses(request, key):

    # all_licenses = models.License.objects.all()
    # str_auth_key = all_licenses

    license = models.License.objects.get(license_code=key)

    # license_info = license
    # str_auth_key = license_info.license_code
    license_info = JsonResponse({
        'product_number': license.product_number,
        'product_order_number': license.product_order_number,
        'email': license.email,
        'phone': license.phone,
        'license_code': license.license_code,
        'start_date': license.start_date,
        'end_date': license.end_date,
        'use_yn': license.use_yn,

    }, json_dumps_params={'ensure_ascii': False})

    # return HttpResponse(content=str_auth_key)
    return license_info

# room = models.Room.objects.get(pk=room_pk)
# reservation = models.Reservation.objects.get_or_none(pk=pk)
# 약간 변경 하여야함 : 있는 수만큼 변수에 루프로 담아서 랜더.
# https://wayhome25.github.io/django/2017/03/19/django-ep3-fbv/
# from django.http import HttpResponse, JsonResponse
# def post_list3(request):
#     return JsonResponse({
#         'message' : '안녕 파이썬 장고',
#         'items' : ['파이썬', '장고', 'AWS', 'Azure'],
#     }, json_dumps_params = {'ensure_ascii': True})
