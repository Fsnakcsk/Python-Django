from django.shortcuts import render, redirect
from member.models import Member
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def add_vip(request):
    return render(request, 'member/join.html')


def insert(request):
    member = Member(user_id = request.POST['user_id'],\
                    user_name = request.POST['user_name'],\
                    user_pass = request.POST['user_pass'],\
                    tel = request.POST['tel'],\
                    email = request.POST['email'])
    member.save()
    return redirect('/')


def login(request):
    db_id = request.POST['user_id']
    db_pwd = request.POST['user_pass']
    id_info = Member.objects.get(user_id=db_id)

    if db_id == id_info.user_id :
        if db_pwd == id_info.user_pass :
            return render(request, 'member/login.html', {'id_info' : id_info})
        else:
            Error = "pwdError"
            return render(request, 'index.html', {'Error' : Error})
    else:
        Error = "idError"
        return render(request, 'index.html', {'Error' : Error})

def logout(request):
    return redirect('/')