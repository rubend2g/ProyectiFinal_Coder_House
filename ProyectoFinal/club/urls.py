from django.urls import path
from club import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('futbol', views.futbol, name='futbol'),
    path('natacion', views.natacion, name='natacion'),
    path('gimnasio', views.gimnasio, name='gimnasio'),
    path('buscar', views.buscar, name='buscar'),
    path('leerNatacion', views.leerNatacion, name = "leerNatacion"),
    path('eliminarNatacion/<natacion_nombre>', views.eliminarNatacion, name = "eliminarNatacion"),
    path('editarNatacion/<natacion_nombre>', views.editarNatacion, name = "editarNatacion"),
    path('leerFutbol', views.leerFutbol, name = "leerFutbol"),
    path('eliminarFutbol/<futbol_nombre>', views.eliminarFutbol, name = "eliminarFutbol"),
    path('editarFutbol/<futbol_nombre>', views.editarFutbol, name = "editarFutbol"),
    path('leerGimnasio', views.leerGimnasio, name = "leerGimnasio"),
    path('eliminarGimnasio/<gimnasio_nombre>', views.eliminarGimnasio, name = "eliminarGimnasio"),
    path('editarGimnasio/<gimnasio_nombre>', views.editarGimnasio, name = "editarGimnasio"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='paginas/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('nosotros', views.nosotros, name='nosotros')

]