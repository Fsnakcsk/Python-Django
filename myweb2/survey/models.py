from django.db import models

# 설문조사 문항
class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)      # 설문 인덱스
    question = models.TextField(null=False)              # 문제
    ans1 = models.TextField(null=True)                   # 보기 1
    ans2 = models.TextField(null=True)                   # 보기 2
    ans3 = models.TextField(null=True)                   # 보기 3
    ans4 = models.TextField(null=True)                   # 보기 4
    status = models.CharField(max_length=1, default='y') # 상태값 (y=진행중, n=중료)

# 설문응답
class Answer(models.Model):
    answer_idx = models.AutoField(primary_key = True)    # 응답인덱스
    survey_idx = models.IntegerField()                   # 설문 객체의 설문인덱스와 연결되는 필드(외래키, Foreign Key)
    num = models.IntegerField()                          # 정답 번호
