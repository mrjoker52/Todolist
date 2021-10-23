from django.urls import path
from .views import * 
# * คือ ดึงมาทุก functions ใน views.py

urlpatterns = [
    path('', Home),
    path('api/all-todolist/',all_todolist),
    path('api/post-todolist', post_todolist),
    path('api/update-todolist/<int:TID>', upate_todolist),
    path('api/delete-todolist/<int:TID>', delete_todolist),
]