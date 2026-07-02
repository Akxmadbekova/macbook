from django.urls import path
from app.views import index, update, delete,iphone_store, update_iphone,delete_iphone

urlpatterns = [
    path("", index, name="index"),
    path("update/<int:id>/",update, name="update"),
    path("delete/<int:id>/",delete, name="delete"), 
    path("iphone/", iphone_store, name="iphone_store"),
    path('/iphone/update/<int:pk>/', update_iphone, name='update_iphone'),  # Tahrirlash
    path('iphone/delete/<int:pk>/', delete_iphone, name='delete_iphone'),
]

