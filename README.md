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