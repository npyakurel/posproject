from django.urls import path
from fcrudapp import views
from .views import *
app_name='fcrudapp'
urlpatterns=[
path('',views.index,name='home'),
path('add/',views.book_create,name='add'),
path('update/<int:pk>/',views.book_update,name='update'),
path('delete/<int:pk>/',views.book_delete,name='delete'),
path('book/<int:pk>/detail/',BookDetailView.as_view(),name='bookdetail'),
path('book/create/',BookCreateView.as_view(),name='bookcreate'),
]