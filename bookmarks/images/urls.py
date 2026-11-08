from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path(
        'detail/<int:id>/<slug:slug>/',
        views.image_detail,
<<<<<<< HEAD
        name='detail',
    ),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
]
=======
        name='detail'
    )
]
>>>>>>> d4dca16e3d65c6052f86761854a51aaddbd630ac
