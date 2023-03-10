from django.db import models
from datetime import datetime

# 매모와 관련된 테이블을 정의하는 클래스
class Memo(models.Model):
    idx = models.AutoField(primary_key=True)
    writer = models.TextField(null=False) # 비어 있으면 안됨
    memo = models.TextField(null=False)
    post_date = models.DateTimeField(default= datetime.now, blank=True)
