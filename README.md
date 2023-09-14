> **Note**
>
> This a is a write up of the process described [here](https://www.youtube.com/watch?v=31R1gSvBn1g&list=PLPSM8rIid1a0SMqmFOfoHRbyfQ5ipQX79) by Legion Script. Notes will be on my understanding rather than following one to one and in short organised bullets when possible.

----

## Contents

### [1. Startup](#startup)
> #### [1.1 Set up the virtual environment](#set-up-the-virtual-environment)
> #### [1.2 Basic installations](#basic-installations)
>#### [1.3 Creating the folder structure and boilerplate](#creating-the-folder-structure-and-boilerplate)

### [2. Creating the API](#creating-the-api)
>#### [2.1 Serializers](#serializers)
>#### [2.2 URLs](#urls)
>#### [2.3 Starting the server](#starting-the-server)

### [3. Creating Models](#creating-models)

-----

## Startup

### Set up the virtual environment

- Create a python virtual enviroment and activate

`python -m venv /path/`

- and then activate with 

`/path to virtual environment folder/Scripts/activate(.bat)`

----

### Basic installations

- The project comes with `Python` and `pip` but we also need `django` and `djangorest-framework`.

`pip install django djangorest-framework`

----

#### Creating the folder structure and boilerplate

- In the destination folder for the project run the command

`django-admin startproject (name)`

- and 

`django-admin startapp (name)`

- navigate to the folder of the project and initialise the database

`./manage.py migrate` 

- and then create a superuser to managa the project with 

`./manage.py createsuperuser`

----

## Creating the API

### Serializers

- Create a `serializers.py` file in the app folder
- Import your models from `django.contrib.auth.models
- Import `serialisers` from `rest-framework`
- Create serializers from models
```py
    class modelSerializer(serializers,HyperlinkedModelSerializers)
        class Meta
            model = Model
            fields = ['field1', 'field2', 'etc etc']
```

or 

```py
    class modelSerializer(serializers,HyperlinkedModelSerializers)
        class Meta
            model = Model
            fields = '__all__'
```

To pass all fields at once all at once.

> **Note**
>
> Hyperlinked uses url instead of primary key. We can also import default django models `User` and `Group` from `django.contrib.auth` to test the function before building our own unique models.

----

### ViewSets 

> **Note**
>
> Use ViewSets to reduce code.

- Create a ViewSet for each model

```py
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by('-default chosen')
    serializer_class = ModelSerializer
    permission_classes = [permissions.IsAuthenticated]
```

----

### URLs 

- Import `path`, `include` from `django.urls`
- Import `router` from `rest-framework`
- Import your views from views folder previously used
- Create a router 

`router = routers.DefaultRouter()`

- Add ViewSets to router

`router.register(r'model', views.ModelViewSet)`

- Delete or coment out the `admin` path
- Add root path and browsable path to the url_patterns

```py 
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

----

### Starting the server

- use the command 

`python ./manage.py runserver`

![rest framework](images/001.png)

----

## Creating models

###

- Import `models` from `django.db`
- Import any defaults from `django.contrib.auth.models`
- Create model class 

```py 
class Model(models.Model):
    field = model.TypeField()
```

> **Note**
>
> Can specify nullable, unique, primary key, etc in parameters

- If enumerables are neccessarily can define them using

```py

#these assigned value are what is sent and displayed to the GUI
#each variable is just a constant of the value shown
OPTION_1 = "1"
OPTION_2 = "2"
OPTION_3 = "3"
OPTION_4 = "4"
OPTION_5 = "5"

#these values are what is sent to the db from the keys given 
#each constant represents the data sent 
OPTION_CHOICES = [
    (OPTION_1, 'one'),
    (OPTION_2, 'two'),
    (OPTION_3, 'three'),
    (OPTION_4, 'four'),
    (OPTION_5, 'five'),
]

field = model.TypeField(choices=OPTION_CHOICES, default=OPTION_3)
```

> **Note**
>
> It's important to make note of the primary key, foreign key and cardinality of each model e.g. many pizzas use different toppings and many toppings can be part of different pizzas so a database schema would have to account for that back and forth.

- Add your app to your backend `setting.py` file

- run the migrations and the server to check everything is correct

- `python ./manage.py makemigrations`

- `python ./manage.py migrate`

- `python ./manage.py runserver`

- Import the models from your app and create serializers in the `serializers.py` file

- Do the same for viewsets

- This time change permissions to also be read only

- `permission_classes = [permissions.IsAuthenticatedOrReadOnly]`

- This allows users to also grab data

- Finally we add this to the router
----


