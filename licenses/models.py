import datetime
from django.db import models
from django.utils import timezone


class License(models.Model):

    """ License Model Definition """

    PRODUCT_DAY = "01d"
    PRODUCT_WEEK = "01w"
    PRODUCT_MONTH = "01m"
    PRODUCT_HALF = "06m"
    PRODUCT_YEAR = "01y"

    PRODUCTS_CHOICES = (
        (PRODUCT_DAY, "1일"),
        (PRODUCT_WEEK, "1주"),
        (PRODUCT_MONTH, "1개월"),
        (PRODUCT_HALF, "6개월"),
        (PRODUCT_YEAR, "1년"),
    )
    product_number = models.CharField(
        max_length=5, choices=PRODUCTS_CHOICES, default=PRODUCT_DAY)
    product_order_number = models.CharField(
        max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    # 0000-00000-00000-0000  20자리
    license_code = models.CharField(max_length=15, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    use_yn = models.BooleanField(default=False)
    event_yn = models.BooleanField(default=False)

    #self.license_code = make__license_code

    def __str__(self):
        return f"{self.email} - {self.phone}"

  # https://velog.io/@inyong_pang/Python-%EC%9E%84%EC%8B%9C%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%83%9D%EC%84%B1


#   https://www.delftstack.com/ko/howto/python/random-string-python/
