from django.shortcuts import render

def home(request):
    # template을 해석하고 실행을 시켜주는 장고의 내장 함수
    # template : html code
    # template : address/templates/index.html
    return render(request, 'index.html')
