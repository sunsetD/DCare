from django.shortcuts import render

# Create your views here.
from .models import Counsel #Post모델 불러오기

def test_view(request):
    posts = Counsel.objects.all() #Post테이블의 모든 객체 불러와서 posts변수에 저장
    print('포스트임',posts)
    return render(request, 'DCare/index.html',{"posts": posts})