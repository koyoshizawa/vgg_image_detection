## 内容
- urlに画像をpostすると、その画像を認識し、その画像に映っているものが何であるのかを返すapi

## やってみたこと
- rest apiを使って機械学習させる
- django-rest-flamework を使用する
- kerasの学習済み画像認識モデルであるvgg16を使用する
- Dockerで開発環境を構築する

## メモ
- djangoプロジェクトを作成する
```bash
$ docker-compose run web django-admin.py startproject composeexample .
```

- データベースの設定をする
```python
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

- コンテナを立ち上げる
```bash
docker-compose up
```

- /item/detection/に画像を投げる
```bash
curl -X POST  http://localhost:8000/item/detection/ -F "image=@/Users/KoYoshizawa/Desktop/dog_img_long-chihuahua.jpg"
```
