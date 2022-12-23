#깃 사용 시 개인정보 노출 방지 차원에서 제작함.
# my_settings.py 파일을 새로 만든다. manage.py와 같은 위치.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'dcare', #2
        'USER': 'OOB', #3
        'PASSWORD': '12345678',  #4
        'HOST': 'localhost',   #5
        'PORT': '3306', #6
    }
}
SECRET_KEY = 'django-insecure-crrwkgvq-uv0j1_6!lc+=g*&g2a_^m3wef(hw4s+6ka+%ln7r9'
