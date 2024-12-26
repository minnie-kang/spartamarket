from django.db import models
from django.contrib.auth.models import AbstractUser

# 프로필 이미지 저장 경로를 설정하는 함수
def user_profile_image_path(instance, filename):
    return f'profile_images/{instance.username}/{filename}'

# 프로필 이미지, 팔로우기능 추가
class User(AbstractUser):
    # 프로필 이미지
    profile_image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)

    # 팔로우 관계
    follows = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    # 팔로워 수를 반환
    @property
    def follower_count(self):
        return self.followers.count()
    
    # 팔로잉 수를 반환
    @property
    def following_count(self):
        return self.follows.count()
    
    def __str__(self):
        return self.username