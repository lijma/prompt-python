from django.urls import path
from .helloworld import chat_gpt
from .prompt import prompt

urlpatterns = [
    path('sample/', chat_gpt, name='chat_gpt'),
    path('prompt/', prompt, name='prompt'),
]
