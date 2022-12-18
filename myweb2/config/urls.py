
from django.contrib import admin
from django.urls import path, re_path, include
from config import views
from django.conf import settings
# from django.conf.urls import url

urlpatterns = [
    # path('요청 url', function)
    # http://localhost
    # http://127.0.01
    path("admin/", admin.site.urls),

    # http://localhost
    path('',views.home),

    # http://localhost/address/
    path('address/', include('address.urls')),

    # http://localhost/memo/
    path('memo/', include('memo.urls')),

    # http://localhost/survey/
    path('survey/', include('survey.urls')),

    # http://localhost/guestbook/
    path('guestbook/', include('guestbook.urls')),

    # http://localhost/member/
    path('member/', include('member.urls')),

# http://localhost/shop/
    path('shop/', include('shop.urls')),

]


# debug 모드로 들어왔다면
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls))
        # path('__debug__/', include(debug_toolbar.urls)),
    ]

    # 장고 라우팅을 구성하는 함스 : path(), url(), re_path()
    # path(요청url, view, function, name=None, kwargs = None)
    # 너머지 두개는 정규표현식 사용할 떄 사용.