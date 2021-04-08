from django.contrib import admin
from . import models
from string import ascii_uppercase, ascii_lowercase, ascii_letters, digits, punctuation
import random


@admin.register(models.License)
class LicenseAdmin(admin.ModelAdmin):
    """ License Admin Definition """

    list_display = (
        "product_order_number",
        "email",
        "phone",
        "license_code",
        "start_date",
        "end_date",
        "use_yn",
        "event_yn",
    )

    list_filter = ("email", "phone", "start_date",
                   "end_date", "use_yn", "event_yn",)

    search_fields = ("email", "phone", "start_date")

    actions = ['make_license_code', 'update_due_date']

    # 위에 액션 하나 더 넣고 거기서 조건부 실행하도록 처리해야함.
    def make_license_code(self, request, queryset):
        updated_count = 0
        for e in queryset:
            # 문자열이 0이면 활성화 코드 부여하고  updated_count +1
            # 문자열ㅇ 0이 아니면 통과
            print(e.license_code)  # --> None
            if e.license_code is None or len(str(e.license_code)) == 0:
                print('worked')
                length_of_string = 10
                temp_code = ''.join(random.SystemRandom().choice(
                    ascii_uppercase + digits) for _ in range(length_of_string))
                #ascii_uppercase, ascii_lowercase, ascii_letters
                e.license_code = temp_code
                e.use_yn = True
                e.save()
                # e.update(license_code=temp_code)

                updated_count = updated_count + 1
                print(temp_code)
            # else:
            #     updated_count = updated_count - 1

        self.message_user(request, '{}건의 활성화코드를 생성하였습니다.'.format(
            updated_count))  # django message framework 활용
    make_license_code.short_description = '[선택라이선스] 활성화'

    def update_due_date(self, request, queryset):
        pass
    update_due_date.short_description = '[사용기한연장 이벤트] 적용'
