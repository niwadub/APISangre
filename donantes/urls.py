from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', views.DonadorView)
router.register(r'lista-usuarios', views.DonadorFiltro)

urlpatterns = [
    # path('', include('donantes.urls'))
    path('', include(router.urls))
]
