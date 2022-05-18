from django.urls import path
from. import views
urlpatterns = [
    path('',views.display,name="display"),
    path('create_form', views.create_form, name="create_form"),
    path('updateForm/<str:pk>/',views.updateForm, name="updateForm"),
    path('deleteForm/<str:pk>/',views.deleteForm, name="deleteForm"),

    ]