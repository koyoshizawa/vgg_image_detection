## やってみたこと
- rest apiを使って機械学習させる
- django-rest-flamework を使用する
- kerasの学習済み画像認識モデルであるvgg16を使用する
- Dockerで開発環境を構築する

```
$ docker-compose run web django-admin.py startproject composeexample .
```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```


```
docker-compose up
```


```
curl -X POST  http://localhost:8000/item/detection/ -F "image=@/Users/KoYoshizawa/Desktop/dog_img_long-chihuahua.jpg"
```
