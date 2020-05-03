from django.urls import path
from .views import (
    AnnounceList,
    AnnounceDetail,
    AnnounceCreate,
    AnnounceUpdate,
    AnnounceDelete
)

app_name = 'announce'
urlpatterns = [
    path('', AnnounceList.as_view(), name='announce-list'),
    path('create/', AnnounceCreate.as_view(), name='announce-create'),
    path('<int:id>/detail', AnnounceDetail.as_view(), name='announce-detail'),
    path('<int:id>/update', AnnounceUpdate.as_view(), name='announce-update'),
    path('<int:id>/delete', AnnounceDelete.as_view(), name='announce-delete'),
]
