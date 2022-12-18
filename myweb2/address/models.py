from django.db import models
# 테이블을 새로 만들려면 models.py 사용해야함
# 하지만 관리자도 해당 어플리케이션을 관리하도록 구현하려면 admin.py에 있는 파일을 수정해야함

class Address(models.Model):
    # 일련번호 이름, 전화, 매일, 주소
    # create table address();  : 데이터베이스에서의 삽입
    # 컬럼명(필드명 = 자료형(속성) : 장고
    # CharField : varchar2와 같다
    # TextField : 굴자수 제한 없음
             # 자동 번호 부여

    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)