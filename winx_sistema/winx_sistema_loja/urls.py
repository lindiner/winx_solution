from django.urls import path
from.import views

urlpatterns = [
    path("", views.home, name="winx_sistema_loja")
]
