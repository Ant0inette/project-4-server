from django.urls import path
from .views import (
    DreamListView,
    DreamDetailView,
    DreamFavoriteView,
    CommentListView,
    CommentDetailView
)

urlpatterns = [
    path('api/dreams/', DreamListView.as_view(), name='dream-list'),
    path('api/dreams/<int:pk>/', DreamDetailView.as_view(), name='book-detail'),
    path('api/dreams/<int:pk>/favorite/', DreamFavoriteView.as_view(), name='/dream-favorite'),
    path('api/dreams/<int:drm_pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('api/dreams/<int:_drm_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view(), name='comment-detail')
]

# reverse('dream-list')
# reverse('dream-detail', kwargs={'pk':1})