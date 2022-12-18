from django.shortcuts import render, redirect
from guestbook.models import Gusstbook


# 검색기능을 구현하는 모듈 추가
from django.db.models import Q #장고에서 갬색할 떄 수행하는 모듈
import math
import os
#from django.utils.http import urlquote


# AND 연산은 filter()내에서 그냥 조건들을 ,쉽표로 조건들을 연결하여 사용
# 하지만 OR 연선은 Q객체와 | 연산자를 사용하여 기술한다
# Guestbook.objects.filter(Q(name__startwith='a')) name라는 필드의 첫번제글자 인 문자들을 검색
# Guestbook.objects.filter(~Q(name__startwith='a')) name라는 필드의 a를 제외하고 검색

def list(request):
    try:
        searchkey = request.POST['searchkey']
    except :
        searchkey = 'name'

    try:
        search = request.POST['search']
    except:
        search = ''

    # __contains : 제약조건
    if searchkey == "name_content":
        gbList = Gusstbook.objects.filter(Q(name__contains = search) | Q(content__contains = search)).order_by('-idx')

    elif searchkey == 'name':
        gbList = Gusstbook.objects.filter(name__contains = search).order_by('-idx')

    elif searchkey == "contant":
        gbList = Gusstbook.objects.filter(content__contains = search).order_by('-idx')

    try:
        msg = request.GET['msg']
    except:
        msg = ''

    return render(request, 'guestbook/list.html', {'gbList':gbList, 'gbCount':len(gbList),
                                                   'searchkey':searchkey, 'search':search, 'msg':msg})

def write(request):
    return render(request, 'guestbook/write.html')


def insert(request):
    row = Gusstbook(name=request.POST['name'], email=request.POST['email'],\
                    passwd=request.POST['passwd'], content=request.POST['content'])

    row.save()
    return redirect('/guestbook')


def passwd_check(request):
    id = request.POST['idx']            # 글번호
    pwd = request.POST['passwd']        # 비빌번호
    row = Gusstbook.objects.get(idx=id) # 입력받은 글번호에 해당하는 방명록 가져오기

    if row.passwd == pwd:               # 비빌번호가 일치한다면
        return render(request, 'guestbook/edit.html', {'row':row})
    else:                               # 비밀번호가 틀리면
        return redirect('/guestbook/?msg=error')


def update(request):
    id = request.POST['idx']
    row = Gusstbook(idx = id, name=request.POST['name'], email=request.POST['email'],\
                              passwd=request.POST['passwd'], content=request.POST['content'])
    row.save()
    return redirect('/guestbook')


def delete(request):
    id = request.POST['idx']
    Gusstbook.objects.get(idx=id).delete()
    return redirect('/guestbook')