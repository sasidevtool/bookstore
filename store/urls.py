from django.conf.urls import url

from store import views
from views import store

urlpatterns = (
    url(r'^$', store, name='index'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
)

