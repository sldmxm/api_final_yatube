from django.urls import path, include
from rest_framework import routers

from api.views import (
    PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet)

app_name = 'api'

router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
