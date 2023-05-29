# from django.db import models
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

# Post가 Model을 상속 받는다. (부모 클래스 Model, 하위 클래스Post)
# 상속 Model의 속성이나 메소드를 Post에서 그대로 쓸 수 있다.
class Post(models.Model):
    # 속성
    # 외래키 - 다른 모델을 가리키는 속성, on_delete author가 지워졌을 경우 Post 테이블의 데이터
    # CASCADE는 author가 지워지면 post도 지워지게
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField 제목이 200자, 길이가 정해져 있는 문자열
    title = models.CharField(max_length=200)
    # TextField 길이가 정해져 있지 않은 문자열
    text = models.TextField()
    # 날짜, 시간
    # timezone.now 현재 시간 (기본값)
    created_date = models.DateTimeField(
            default=timezone.now)
    # published_date 게시글이 게시된 날짜
    published_date = models.DateTimeField(
            blank=True, null=True)

    #메서드
    def publish(self):
        # self 자기 자신의 오브젝트를 가리키는 약속
        self.published_date = timezone.now()
        self.save()
    #메서드
    def __str__(self):
        return self.title