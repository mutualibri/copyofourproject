from django.urls import path, include
from book.views import get_books_by_json, get_books_by_xml, register, login_user, logout_user, show_main, search, get_product_json, create_lend_flutter

app_name = 'book'

urlpatterns = [
    path('json/', get_books_by_json, name='get_book_by_jsons'),
    path('xml/', get_books_by_xml, name='get_by_xml'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('search/', search, name='searchbar'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-lend-flutter/', create_lend_flutter, name="create_lend_flutter"),
]