from django.urls import path
from app.views import index, update, delete,iphone_store

urlpatterns = [
    path("", index, name="index"),
    path("update/<int:id>/",update, name="update"),
    path("delete/<int:id>/",delete, name="delete"), 
    path("iphone/", iphone_store, name="iphone_store")
]

