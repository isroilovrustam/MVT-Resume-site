from django.urls import path
from .views import indexView, aboutView, serviceView, blogView, contactView, collectionView, detailView

urlpatterns = [
    path('', indexView, name='index'),
    path('about/', aboutView, name='about'),
    path('collection/', collectionView, name='collection'),
    path('service/', serviceView, name='service'),
    path('blog/', blogView, name='blog'),
    path('blog/<int:pk>/', detailView, name='detail'),
    path('contact/', contactView, name='contact'),
]