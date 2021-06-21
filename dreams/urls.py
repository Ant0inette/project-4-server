from django.urls import path
from .views import (
    DreamListView,
    DreamDetailView,
    DreamFavoriteView,
    CommentListView,
    CommentDetailView    
)

urlpatterns = [
    path('', DreamListView.as_view()),
    path('<int:pk>/', DreamDetailView.as_view()),
    path('<int:pk>/favorite/', DreamFavoriteView.as_view()),
    path('<int:drm_pk>/comments/', CommentListView.as_view()),
    path('<int:_drm_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view()),
    
]

# reverse('dream-list')
# reverse('dream-detail', kwargs={'pk':1})