from django.urls import path
from .views import welcome, detail_view, category_view, contact_view


urlpatterns = [
    path('', welcome, name='welcome page'),
    path('<int:id>', detail_view, name = 'detail'),
    path('category/<str:name>', category_view, name='category'),
    path('contact', contact_view, name='contact'),


]