from django.shortcuts import render, redirect
from address.models import Address


def home(request) :
    # http://localhost/address 요청을 받고 화면에 보여줄 내용을 기술하는 영역
    #  주소록에 저장된 모든 주소록을 가져오고
    # select * from address
    items = Address.objects.order_by('-idx')

    # 가져온 주소록을 화면에 출력하는 웹피이지를 제작
    # 그것을 응답으로 되돌려주는 작업을 수행
    return render(request, 'address/list.html', {'items':items, 'count':len(items)})


def write(request):
    # 입력받는 품을 가지고 있는 웹피이지를 반환한다.
    # http://localhost/address/write
    return(request,'address/write.html')


def insert(request):
    # http://localhost/address/insert
    # write.html체이지에서 입력받은 <form>품을 가져와서
    addr = Address(name = request.POST['name'], tel = request.POST['tel'],\
                   email = request.POST['email'], address = request.POST['address'])

    # 데이터베이스에 정장
    addr.save()

    # 주소록의 시작화면으로 이동
    return redirect('/address')


def detail(request):
    # 주소록에 저장된 특정 레코드의 내용을 상세보기
    id = request.GET['idx']
    addr = Address.objects.get(idx = id)  # 데이터베이스에서 특정 레코드를 가지고 와야함.
    return render(request, 'address/detail.html',{'addr':addr}) # 하나의 주소록 정보를 웹페이지로 전달


def update(request):
    id = request.POST['idx']
    addr = Address(idx = id, name = request.POST['name'], tel = request.POST['tel'],\
                   email = request.POST['email'], address = request.POST['address'])
    addr.save()
    return redirect('/address')


def delete(request):
    id = request.POST['idx']
    Address.objects.get(idx = id).delete()
    return redirect('/address')
