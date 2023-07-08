from django.urls import path

from . import views

app_name = 'problems'

urlpatterns = [
    path('<int:pk>/', views.problems, name='problems'),
    path('<int:pk>/<int:id>/', views.detail, name='problem'),
    path('all_problems/', views.all_problems, name='all_problems'),
    # path('new_category/', views.new_category, name='new_category'),
    # path('new_item/', views.new_item, name='new_item'),
    # path('sell/<int:pk>/<int:id>', views.mark_item_as_sold, name='sell'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
]