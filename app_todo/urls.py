from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='adding'),
    path('done/<int:task_id>', views.done, name='done'),
    path('delete/<int:task_id>', views.delete, name='delete')
]