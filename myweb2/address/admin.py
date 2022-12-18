from django.contrib import admin
from address.models import Address

# Admin 사이트에 반영할 테이블에 필드를 정의
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'email', 'address')

# 최상인 개체인 admin에게 등록해야함
admin.site.register(Address,AddressAdmin)

