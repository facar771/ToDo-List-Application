from django.urls import path , include # eklenen
from . import views
#from register import views as v

urlpatterns = [
    path('', views.index,name="index"),
    path('login/', views.login,name="login"),
    #path('', include("django.contrib.auth.urls")),  # eklenen
    #path("register/", v.register, name="register"),  # eklenen
    path('about/', views.about,name="about"),
    path('create/', views.create,name="create"),
    path('delete/<Todos_id>', views.delete,name="delete"),
    path('yes_finish/<Todos_id>', views.yes_finish,name="yes_finish"),
    path('no_finish/<Todos_id>', views.no_finish,name="no_finish"),
    path('update/<Todos_id>', views.update,name="update"),

]