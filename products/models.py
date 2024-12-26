from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import re

# 상품 이미지를 저장할 경로를 생성하는 함수
def product_image_path(instance, filename):
    # 사용자별로 상품 이미지를 저장할 경로를 생성
    return f'product_images/{instance.user.username}/{filename}'

# 해시태그가 유효한지 검사한는 사용자 정의 함수
def validation_hashtag(value):
    # 정규표현식을 사용하여 해시태그가 알파벳, 숫자, 언더스코어만 포함되도록
    if not re.match(r'^[0-9a-zA-Z_]+$', value):
        raise ValidationError('해시태그는 알파벳, 숫자, 언더스코어만 가능합니다.')

# 해시태그를 저장하는 모델
class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[validation_hashtag])
    # 해시태그 객체를 출력할 때 '#(해시태그명)' 형태로 반환
    def __str__(self):
        return f'#({self.name})'

# 사용자의 등록한 상품을 저장하는 모델
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_products', blank=True)
    hashtags = models.ManyToManyField(HashTag, related_name='products', blank=True)
    views = models.PositiveIntegerField(default=0)
    
    # 상품에 좋아요를 누른 사용자 수 반환
    def like_count(self):
        return self.likes.count()

    # 상품 객체를 출력할 때 상품 제목을 반환
    def __str__(self):
        return self.title