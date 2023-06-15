from django.urls import path
from .views import PostListApiView, PostCreateApiView, PostRetrieveUpdateDestroyApiView, PostCommentLIstApiView,\
    PostCommentCreateApiView, CommentListApiView, PostLikeListApiView, CommentRetrieveApiView, \
    CommentLikeListApiView, PostLikeApiView, CommentLikeApiView


urlpatterns = [
    path('list/', PostListApiView.as_view()),
    path('create/', PostCreateApiView.as_view()),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyApiView.as_view()),
    path('<uuid:pk>/likes/', PostLikeListApiView.as_view()),
    path('<uuid:pk>/comments/', PostCommentLIstApiView.as_view()),
    path('<uuid:pk>/comments/create/', PostCommentCreateApiView.as_view()),

    path('comments/', CommentListApiView.as_view()),
    path('comments/<uuid:pk>/', CommentRetrieveApiView.as_view()),
    path('comments/<uuid:pk>/likes/', CommentLikeListApiView.as_view()),

    path('<uuid:pk>/create-delete-like/', PostLikeApiView.as_view()),
    path('<uuid:pk>/create-delete-commentlike/', CommentLikeApiView.as_view())

]
