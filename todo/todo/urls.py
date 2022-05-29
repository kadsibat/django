from django.urls import path
<<<<<<< HEAD
from .views import home, todo_list,todo_create,todo_update,todo_delete
=======
from .views import home, todo_list, todo_create, todo_update, todo_delete

>>>>>>> 43779547f62600caefec0fad8d720af6d9000752
urlpatterns = [
    path("", home, name="home"),
    path("list/", todo_list, name="list"),
    path("add/", todo_create, name="add"),
    path("update/<int:id>/", todo_update, name="update"),
<<<<<<< HEAD
     path("delete/<int:id>/", todo_delete, name="delete"),
=======
    path("delete/<int:id>/", todo_delete, name="delete"),
>>>>>>> 43779547f62600caefec0fad8d720af6d9000752
]
