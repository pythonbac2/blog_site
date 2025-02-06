from django.urls import path
from .views import book_list, second_view, pages

urlpatterns = [
    path('', book_list, name="book_page"),
    path('second/', second_view, name='second_page'),
    path('pages/<str:page>', pages, name='pages'),
]