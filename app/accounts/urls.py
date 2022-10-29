from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, UserView, UserChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserView.as_view(), name='user_detail'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='user_change')
]
