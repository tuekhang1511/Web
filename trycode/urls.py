from django.urls import path

from . import views

app_name = 'try_code'

urlpatterns = [
    path('detail/<int:id>', views.try_code, name='detail'),
]