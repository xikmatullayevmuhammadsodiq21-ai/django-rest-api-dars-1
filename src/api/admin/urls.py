
from django.urls import path
from api.admin.views.users_list import UserListApiView
from api.admin.views.book_list import BookListApiView
from api.admin.views.author_list import AuthorListApiView
from api.admin.views.my_list import MyListApiView
from api.admin.views.book_create import BookCreatetApiView
from api.admin.views.book_update_1 import BookUpgradetApiView
from api.admin.views.book_delete import BookDeletetApiView
from api.admin.views.author_login import AuthorLoginApiView
from api.admin.views.author_register import AuthorRegisterApiView
from api.admin.views.author_logout import AuthorLogoutApiView

urlpatterns = [
    path("user/list/", UserListApiView.as_view()),
    path("book/list/", BookListApiView.as_view()),
    path("author/list/", AuthorListApiView.as_view()),
    path("my/list/", MyListApiView.as_view()),
    path("book/create/", BookCreatetApiView.as_view()),
    path("book/upgrade/", BookUpgradetApiView.as_view()),
    path("book/delete/", BookDeletetApiView.as_view()),
    path("author/logout/", AuthorLogoutApiView.as_view()),
]

