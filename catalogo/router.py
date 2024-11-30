from django.urls import path

from user.apiview_controller import API_User

router_user = [
    path('user', API_User.as_view(), name='user')
]