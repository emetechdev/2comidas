from django.urls import path

from credential.apiview_controller import API_Credential

router_credential = [
    path('credential', API_Credential.as_view(), name='credential')
]