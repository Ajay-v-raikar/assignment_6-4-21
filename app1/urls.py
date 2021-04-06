from django.urls import path
from app1 import views 

urlpatterns = [
    path('',views.sample,name='sample'),
    path('<data>',views.display,name='display'),
    path('add/<num1>/<num2>',views.addition,name='add'),
    path('fact/<num>',views.factorial,name='fact'),
    path('operate/<data>',views.operation,name='operate'),
]

