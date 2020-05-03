from django.urls import path
from .views import (
    AnnounceList,
    AnnounceDetail,
    AnnounceCreate,
    AnnounceUpdate,
)

app_name = 'announce'
urlpatterns = [
    path('', AnnounceList.as_view(), name='announce-list'),
    path('create/', AnnounceCreate.as_view(), name='announce-create'),
    path('<int:id>/detail', AnnounceDetail.as_view(), name='announce-detail'),
    path('<int:id>/update', AnnounceUpdate.as_view(), name='announce-update'),
]
