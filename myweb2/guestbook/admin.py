from django.contrib import admin
from guestbook.models import Gusstbook

class GuestbookAdmin(admin.ModelAdmin) :
    # 관리자 사이트에서 방명록을 관리할 필드의 목록을 튜풀로 정의
    list_display = ('name', 'email', 'passwd', 'content')

admin.site.register(Gusstbook, admin.ModelAdmin)
