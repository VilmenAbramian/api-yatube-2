from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_ver1 = SimpleRouter()
router_ver1.register(r'posts/(?P<post_id>\d+)/comments',
                     CommentViewSet,
                     'comment')
router_ver1.register(r'follow', FollowViewSet, 'follow')
router_ver1.register(r'groups', GroupViewSet, 'groups')
router_ver1.register(r'posts', PostViewSet, 'posts')


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_ver1.urls)),
]
