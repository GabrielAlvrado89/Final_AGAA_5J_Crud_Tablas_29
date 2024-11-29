from django.urls import path
from marcas_app import views 

urlpatterns = [
    path("marcas", views.inicio_Marcas, name="marcas"),
    path("registrarMarcas/",views.registrarMarcas,name="registrarMarcas"),
    path('seleccionarMarcas/<id_marcas>', views.seleccionarMarcas, name='seleccionarMarcas'),
    path('editarMarcas/', views.editarMarcas, name='editarMateria'),
    path('borrarMarcas/<id_marcas>', views.borrarMarcas, name='borrarMarcas' ),
]