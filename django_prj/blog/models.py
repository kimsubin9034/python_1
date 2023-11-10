import os

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50) #제목
    hook_text = models.CharField(max_length=100, blank=True) #요약문
    content = models.TextField()            #내용
    # 해당 폴더를 만들어서 년,월,일로 내려가서 저장하도록 설정하도록 설정
    # blank = True : 빈칸 가능, 필수 기능 아님
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d' , blank= True)
    #파일 업로드
    file_upload = models.FileField(upload_to='blog/images/%Y/%m/%d' , blank= True)
    created_at  = models.DateTimeField(auto_now_add=True)    #작성일
    updated_at = models.DateTimeField(auto_now=True)
    #author : 작성자 추후 작성

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    #사용자 정의 함수
    #get_absolute_url은 장고에서 권장하는 관례
    #모델의 인스턴스를 대표하는 URL을 반환하기 위해
    #get_absolute_url()을 작성하는 것을 권장
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # os.path.basename : 주어진 경로 문자열에서 파일 또는 디렉토리의
    # 기본이름을 추출하는 함수이더다.
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split(',')[-1]