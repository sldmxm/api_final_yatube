from rest_framework import viewsets, filters, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Group
from api.serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
)
from api.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    # логично было бы оставить в модели обратную сортировку,
    # а здесь сделать прямую, чтобы не портить воображаемую выдачу в html,
    # но так тесты тоже не проходят, хотя все работает
    # upd. если делать разные сортировки здесь и в модели,
    # тесты не проходят, я это имел в виду выше
    queryset = Post.objects.order_by('pk',)
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    # можно сделать, конечно, поиск по полному совпадению,
    # но решил выбрать компромиссный вариант,
    # а сделать case-sensitive поиск по латинице на sqlite,
    # похоже, нестандартная история
    search_fields = ('^following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )
