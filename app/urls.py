from django.urls import path,include
from app import views


urlpatterns = [
    path('',views.index,name="index"),

    path('add',views.add,name="add"),
    path('delete/',views.deleteAll,name="deleteall"),
    path('completed/<int:pk>',views.completed,name="completed"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('not_completed/<int:pk>',views.not_completed,name="not_completed"),
    path('important/<int:pk>',views.important,name="important"),
    path('not_important/<int:pk>',views.not_important,name="not_important"),


]
