from django.urls import path
from .views import dashboard
from apps.bookmark.views import categories, category
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('categories', categories, name='categories'),
    path('categories/<int:category_id>/', category, name='category')
]
