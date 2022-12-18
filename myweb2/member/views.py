from django.shortcuts import render, redirect

# 장고가 가지고 있는 데이터베이스의  user
from django.contrib.auth.models import User # 장고가 이미 만든 로그인 로그옷 들.. 유효성검사까지 등.. 제공
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin, logout as dlogout

#클래스를 form으로 만든 것을 가져옴
from member.models import UserForm, LoginForm


def home(request):
    # 로그인을 하지 않는 상태라면
    if not request.user.is_authenticated:
        data = {'username':request.user, 'is_authenticated':request.user.is_authenticated}

    # 로그인을 한 상태라면
    else:
        data = {'last_login':request.user.last_login,
                'username':request.user.username,
                'password':request.user.password,
                'is_authenticated':request.user.is_authenticated}

    return render(request, 'member/index.html',{'data':data})


# 회원가입 처리
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        # 입력값에 문자가 없다면(모든 유효성검증 규칙을 종과했바면
        if form.is_valid():
            # 유효성검사함수 user객체에 존재하느냐
            # form.cleaned_date : 검증에 성공한 값들을 딕셔너리 타입으로 저장하고 있는 데이터
            # **변수 : 키워드 변수(key, vlaue)
            new_user = User.objects.create_user(**form.cleaned_data) # 새로운 사용자가 갱성됨

            # 로그인 처리
            dlogin(request, new_user)

            # 시작페이지로 이동
            return redirect('/member')
        else:
            return render(request, 'member/index.html',{'msg':'회원가입 실패'})

    else:
        # post 방식이 아닌 경우 -> 회원가입페이지로 이동.
        form = UserForm()
        return render(request, 'member/join.html',{'form':form})

def login_check(request):
    if request.method == "POST":
        name = request.POST['username']
        pwd = request.POST['password']

        # 인증처리
        user = authenticate(username=name, password=pwd)
        if user is not None:
            dlogin(request, user)
            # session에 저장
            request.session['userid'] = name
            return redirect('/member')
        else:
            return render(request, 'member/index.html', {'msg':'로그인 실패'})
    else :
        form = LoginForm()
        return render(request, 'member/login.html', {'form':form})


def logout(request):
    # 로그아웃 처리를 위한 로직
    dlogout(request) # 세션을 비우는 작업
    return redirect('/member')