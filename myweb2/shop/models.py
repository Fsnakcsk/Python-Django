from django.db import models


# 상품관련 클래스
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(null=False, max_length=150)
    price = models.IntegerField(default=0)
    description = models.TextField(null=False, max_length=150) # 상품 설명
    picture_url = models.CharField(null=True, max_length=150)  # 상품 이미지


# 장바구니 관련 클래스
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)            # 바구니 번호
    userid = models.CharField(null=False, max_length=150)   # 어떤 고객id
    product_id = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)                 # 수량