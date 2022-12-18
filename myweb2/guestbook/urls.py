from django.urls import path
from guestbook import views

# 방명록 관련 urls - 매필값
urlpatterns = [
    path('', views.list),                    # http://localhost/guestbook
    path('write', views.write),              # http://localhost/guestbook/wirte
    path('gb_insert', views.insert),
    path('passwd_check', views.passwd_check),
    path('gb_update', views.update),
    path('gb_delete', views.delete),
]