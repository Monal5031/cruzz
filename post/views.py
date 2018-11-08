# django
from rest_framework import generics, mixins, status
from rest_framework.exceptions import NotFound
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

# local django
from post.models import Post, Comment, Tag
from post.renderers import PostJSONRenderer, CommentJSONRenderer
from post.serializers import PostSerializer, CommentSerializer, TagSerializer


class PostCreateView(mixins.CreateModelMixin, GenericAPIView):
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (PostJSONRenderer,)
    serializer_class = PostSerializer

    def post(self, request):
        serializer_context = {
            'author': request.user.username,
            'request': request
        }
        serializer_data = request.data.get('post', {})
        serializer = self.serializer_class(data=serializer_data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDisplayView(mixins.ListModelMixin, GenericAPIView):
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.select_related('author', 'author__user')
    renderer_classes = (PostJSONRenderer,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)

        if author is not None:
            queryset = queryset.filter(author__user__username=author)

        tag = self.request.query_params.get('tag', None)

        if tag is not None:
            queryset = queryset.filter(tags__tag=tag)

        favorited_by = self.request.query_params.get('favorited', None)

        if favorited_by is not None:
            queryset = queryset.filter(favorited_by__user__username=favorited_by)

        return queryset

    def get(self, request):
        serializer_context = {'request': request}
        page = LimitOffsetPagination()
        paginated_result = page.paginate_queryset(self.get_queryset(), request)

        serializer = self.serializer_class(paginated_result, context=serializer_context, many=True)

        new_data = {
            'posts': serializer.data
        }

        return Response(new_data)


class PostSingleView(mixins.RetrieveModelMixin, GenericAPIView):
    lookup_field = 'slug'
    queryset = Post.objects.select_related('author', 'author__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (PostJSONRenderer,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)

        if author is not None:
            queryset = queryset.filter(author__user__username=author)

        tag = self.request.query_params.get('tag', None)

        if tag is not None:
            queryset = queryset.filter(tags__tag=tag)

        favorited_by = self.request.query_params.get('favorited', None)

        if favorited_by is not None:
            queryset = queryset.filter(favorited_by__user__username=favorited_by)

        return queryset

    def get(self, request, post_slug=None):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=post_slug)
        except Post.DoesNotExist:
            raise NotFound("A post with this slug does not exist.")

        serializer = self.serializer_class(serializer_instance, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUpdateView(mixins.RetrieveModelMixin, GenericAPIView):
    lookup_field = 'slug'
    queryset = Post.objects.select_related('author', 'author__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (PostJSONRenderer,)
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)

        if author is not None:
            queryset = queryset.filter(author__user__username=author)

        tag = self.request.query_params.get('tag', None)

        if tag is not None:
            queryset = queryset.filter(tags__tag=tag)

        favorited_by = self.request.query_params.get('favorited', None)

        if favorited_by is not None:
            queryset = queryset.filter(favorited_by__user__username=favorited_by)

        return queryset

    def post(self, request, post_slug=None):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=post_slug)
        except Post.DoesNotExist:
            raise NotFound("A post with this slug does not exist.")

        serializer_data = request.data.get('post', {})

        serializer = self.serializer_class(
            serializer_instance, context=serializer_context,
            data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsListCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'post__slug'
    lookup_url_kwarg = 'post_slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.select_related('post', 'post__author', 'post__author__user', 'author', 'author__user')
    renderer_classes = (CommentJSONRenderer,)
    serializer_class = CommentSerializer

    def filter_queryset(self, queryset):
        # only want comments for a specific post
        filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}

        return queryset.filter(**filters)

    def create(self, request, post_slug=None):
        data = request.data.get('comment', {})
        context = {'author': request.user.profile}

        try:
            context['post'] = Post.objects.get(slug=post_slug)
        except Post.DoesNotExist:
            raise NotFound("A post with this slug does not exist.")

        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentsDestroyAPIView(generics.DestroyAPIView):
    lookup_url_kwarg = 'comment_pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()

    def destroy(self, request, post_slug=None, comment_pk=None):
        try:
            comment = Comment.objects.get(pk=comment_pk)
        except Comment.DoesNotExist:
            raise NotFound("A comment with this ID does not exist.")

        comment.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PostsFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (PostJSONRenderer,)
    serializer_class = PostSerializer

    def delete(self, request, post_slug=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            post = Post.objects.get(slug=post_slug)
        except Post.DoesNotExist:
            raise NotFound("A post with this slug was not found.")

        profile.unfavorite(post)

        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_slug=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            post = Post.objects.get(slug=post_slug)
        except Post.DoesNotExist:
            raise NotFound("A post with this slug was not found.")

        profile.favorite(post)

        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer

    def list(self, request):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({'tags': serializer.data}, status=status.HTTP_200_OK)


class PostsFeedAPIView(mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    renderer_classes = (PostJSONRenderer,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            author__in=self.request.user.profile.follows.all()
        )

    def get(self, request):
        serializer_context = {'request': request}
        page = LimitOffsetPagination()
        paginated_result = page.paginate_queryset(self.get_queryset(), request)

        serializer = self.serializer_class(paginated_result, context=serializer_context, many=True)

        new_data = {
            'posts': serializer.data
        }

        return Response(new_data)
