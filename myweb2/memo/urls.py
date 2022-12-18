from django.urls import path
from memo import views

# 메모장 관련 urls 등록
# pathon(url요청, function)

urlpatterns = [
    # http://localhost/memo
    path('', views.home),

    # http://localhost/memo/insert_memo
    path('insert_memo', views.insert_memo),

    # http://localhost/memo/detail_memo
    path('detail', views.detail_memo),

    # http://localhost/memo/update_memo
    path('update_memo', views.update_memo),

    # http://localhost/memo/delete_memo
    path('delete_memo', views.delete_memo),

]