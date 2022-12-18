from django.shortcuts import render, redirect
from shop.models import Product, Cart


UPLOAD_DIR ="C:/k_digital/source/Web/myweb2/shop/static/images/"

# session 객체에 담을 때 request.session['key'] = 값
# session 객체에 있는 값을 가져올 떄 request.session.get('key') key값 없을 떄 뒤에 값을 넘긴다
# session.session.get('userid', False) : userid라는 키값이 세션에 있다면 가져오고 없다면 False담는다.

def product_list(request):
    productList = Product.objects.order_by('product_name')                        # 상품 테이블에 저장된 모든 상품을 가져와
    return render(request, 'shop/product_list.html', {'productList':productList,  # 가져온 객체를 출력한 템플릿으로 전달(객체,건수)
                                                      'count':len(productList)})


def product_write(request):
    # 상품을 등록하는 품을 반환해주는 함수, 단 세션에 값이 존재할 때만 수행하도록 구현
    if request.session.get('userid', False):
        return render(request, 'shop/product_write.html')
    else:
        return redirect('/member/login')


def product_insert(request):
    # 상품등록품을 통해 입력받은 값을 객체화해서 DB에 전당하는 작업
    # 상품이미지가 파일로 전달된다.
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file._name
        fp = open("%s%s" % (UPLOAD_DIR, file_name), "wb") # binary write **이미지니까 이진수로 가져옴**

        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    else:
        file_name = '-'

    row = Product(product_name = request.POST['product_name'],
                  description = request.POST['description'],
                  price = request.POST['price'],
                  picture_url = file_name)
    row.save()
    return redirect('/shop/product_list')


def product_detail(request):
    # 특정 상품의 상세보기
    pid = request.GET['product_id']
    row = Product.objects.get(product_id=pid)   # 전달받은 상품일련번호에 해당하는 상품을 가져온다.
    return render(request, 'shop/product_detail.html', {'row':row, 'range':range(1, 21)})



def product_update(request):
    # 등록된 상품을 숭정하는 작업
    id = request.POST['product_id']
    row_src = Product.objects.get(product_id=id)

    p_url = row_src.picture_url
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        p_url = file._name
        fp = open("%s%s" % (UPLOAD_DIR, p_url), "wb") # binary write **이미지니까 이진수로 가져옴**

        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    row_new = Product(product_id = id,
                      product_name = request.POST['product_name'],
                      description = request.POST['description'],
                      price = request.POST['price'],
                      picture_url = p_url)

    row_new.save()
    return redirect('/shop/product_list')


def product_delete(request):
    id = request.POST['product_id']
    Product.objects.get(product_id=id).delete()
    return redirect('/shop/product_list')


def product_edit(request):
    if request.session.get('userid', False):
        pid = request.GET['product_id']
        row = Product.objects.get(product_id=pid)
        return render(request, 'shop/product_edit.html', {'row':row})
    else:
        return redirect('/member/login')

#----------------------------------------------------------------------------------------------------------


def cart_insert(request):
    uid = request.session.get('userid','') #혹은 False
    if uid != "": # is no None
        row = Cart(userid=uid,
                   product_id=request.POST['product_id'],
                   amount=request.POST['amount'],)
        row.save()
        return redirect('/shop/cart_list') # 장바구니목록으로 이동
    else:
        return redirect('/member/login')


def cart_list(request):
    # 장바구니 목록
    uid = request.session.get('userid','')
    if uid != '':
        cartList = Cart.objects.raw("""
            SELECT cart_id, userid, amount, c.product_id, product_name, price, amount*price money
            FROM shop_cart c, shop_product p
            WHERE c.product_id = p.product_id and userid = '{0}'
        """.format(uid))


        sumMoney = 0 # 총금액 : money들의 총금액(물품금액), 배송료 미포함
        fee = 0      # 배송료
        total = 0    # 총금액 : 배송료 포함

        cartCount = len(cartList)
        if cartCount > 0:
            for item in cartList:
                sumMoney += item.money # 총 구매금액
            # 매송료
            if sumMoney != None and sumMoney >= 50000:
                fee = 0
            else:
                fee = 3000

            # 매송료 포함 총금액
            if sumMoney != None:
                total = sumMoney + fee
            else:
                total = 0
                sumMoney = 0

        return render(request, 'shop/cart_list.html', {'cartList':cartList,
                                                        'cartCount':len(cartList),
                                                        'sumMoney':sumMoney,
                                                        'fee':fee, 'total':total})
    else:
        return redirect('/member/login')


def cart_update(request):
    uid = request.session.get('userid', '')
    if uid != '':
        # getlist() : form에서 input 값으로 여러개의 값을 받아서 처리할 때 사용
        amt = request.POST.getlist('amount')
        cid = request.POST.getlist('cart_id')
        pid = request.POST.getlist('product_id')
        for idx in range(len(cid)):
            row = Cart(cart_id=cid[idx], userid=uid, product_id=pid[idx], amount=amt[idx])
            row.save()
        return redirect('/shop/cart_list')
    else:
        return redirect('/member/login')

def cart_del(request):
    Cart.objects.get(cart_id=request.GET['cart_id']).delete()
    return redirect('/shop/cart_list')


def cart_del_all(request):
    uid = request.session.get('userid', '')
    if uid != '':
        Cart.objects.filter(userid=uid).delete()
        return redirect('/shop/cart_list')
    else:
        return redirect('/member/logoin')