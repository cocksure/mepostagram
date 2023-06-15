from django.urls import path
from .views import CreateUserView, VerifyApiView, GetNewVerification, ChangeUserInformationView,\
    ChangeUserPhotoView, LoginView, LoginRefreshView, LogoutView, ForgotPasswordView, ResestPasswordView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('login/refresh/', LoginRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyApiView.as_view()),
    path('new-verify/', GetNewVerification.as_view()),
    path('change-user/', ChangeUserInformationView.as_view()),
    path('change-user-photo/', ChangeUserPhotoView.as_view()),
    path('forgot-passsword/', ForgotPasswordView.as_view()),
    path('reset-passsword/', ResestPasswordView.as_view()),
]
