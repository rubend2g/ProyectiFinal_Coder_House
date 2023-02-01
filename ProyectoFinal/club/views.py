from django.shortcuts import render
from django.http import HttpResponse
from club.forms import futbolFormulario, gimnasioFormulario, natacionFormulario, UserRegisterForm, UserEditForm
from club.models import Futbol, Natacion, Gimnasio, Actividad
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'paginas/inicio.html')

def futbol(request):

      if request.method == 'POST':

            miFormulario = futbolFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  InscripcionFutbol = Futbol (nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], actividad=informacion['actividad']) 

                  InscripcionFutbol.save()

                  return render(request, "paginas/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= futbolFormulario() #Formulario vacio para construir el html

      return render(request, "paginas/futbol.html", {"miFormulario":miFormulario})


def natacion(request):

      if request.method == 'POST':

            miFormulario = natacionFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  InscripcionNatacion = Natacion (nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], actividad=informacion['actividad'])

                  InscripcionNatacion.save()

                  return render(request, "paginas/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= natacionFormulario() #Formulario vacio para construir el html

      return render(request, "paginas/natacion.html", {"miFormulario":miFormulario})

def gimnasio(request):

      if request.method == 'POST':

            miFormulario = gimnasioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  InscripcionGimnasio = Gimnasio (nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], actividad=informacion['actividad'])

                  InscripcionGimnasio.save()

                  return render(request, "paginas/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= gimnasioFormulario() #Formulario vacio para construir el html

      return render(request, "paginas/gimnasio.html", {"miFormulario":miFormulario})

def buscar(request):

      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['nombre'] 
            actividad = actividad.objects.filter(nombre__icontains=nombre)

            return render(request, "paginas/inicio.html", {"actividad":actividad, "nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def leerNatacion(request):
      sociosNatacion = Natacion.objects.all() #trae todos los profesores
      contexto= {"sociosNatacion":sociosNatacion} 
      return render(request, "paginas/leerNatacion.html",contexto)

def eliminarNatacion(request, natacion_nombre):
      sociosNatacion = Natacion.objects.get(nombre=natacion_nombre)
      sociosNatacion.delete()
      # vuelvo al menú
      sociosNatacion = Natacion.objects.all()  # trae todos los profesores
      contexto = {"SociosNatacion": sociosNatacion}
      return render(request, "paginas/inicio.html", contexto)

def editarNatacion(request, natacion_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    natacion = Natacion.objects.get(nombre=natacion_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = natacionFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            natacion.nombre = informacion['nombre']
            natacion.apellido = informacion['apellido']
            natacion.dni = informacion['dni']
            natacion.actividad = informacion['actividad']

            natacion.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "paginas/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
      miFormulario = natacionFormulario(initial={'nombre': natacion.nombre, 'apellido': natacion.apellido,
                                                   'dni': natacion.dni, 'actividad': natacion.actividad})

    # Voy al html que me permite editar
    return render(request, "paginas/natacion.html", {"miFormulario": miFormulario, "natacion_nombre": natacion_nombre})

def leerFutbol(request):
      sociosFutbol = Futbol.objects.all() #trae todos los profesores
      contexto= {"sociosFutbol":sociosFutbol} 
      return render(request, "paginas/leerFutbol.html",contexto)

def eliminarFutbol(request, futbol_nombre):
      sociosFutbol = Futbol.objects.get(nombre=futbol_nombre)
      sociosFutbol.delete()
      # vuelvo al menú
      sociosFutbol = Natacion.objects.all()  # trae todos los profesores
      contexto = {"Sociosfutbol": sociosFutbol}
      return render(request, "paginas/inicio.html", contexto)

def editarFutbol(request, futbol_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    futbol = Futbol.objects.get(nombre=futbol_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = natacionFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            futbol.nombre = informacion['nombre']
            futbol.apellido = informacion['apellido']
            futbol.dni = informacion['dni']
            futbol.actividad = informacion['actividad']

            futbol.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "paginas/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
      miFormulario = natacionFormulario(initial={'nombre': futbol.nombre, 'apellido': futbol.apellido,
                                                   'dni': futbol.dni, 'actividad': futbol.actividad})

    # Voy al html que me permite editar
    return render(request, "paginas/futbol.html", {"miFormulario": miFormulario, "natacion_nombre": futbol_nombre})

def leerGimnasio(request):
      sociosGimnasio = Gimnasio.objects.all() #trae todos los profesores
      contexto= {"sociosGimnasio":sociosGimnasio} 
      return render(request, "paginas/leerGimnasio.html",contexto)

def eliminarGimnasio(request, gimnasio_nombre):
      sociosGimnasio = Gimnasio.objects.get(nombre=gimnasio_nombre)
      sociosGimnasio.delete()
      # vuelvo al menú
      sociosGimnasio = Gimnasio.objects.all()  # trae todos los profesores
      contexto = {"sociosGimnasio": sociosGimnasio}
      return render(request, "paginas/inicio.html", contexto)

def editarGimnasio(request, gimnasio_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    gimnasio = Gimnasio.objects.get(nombre=gimnasio_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = natacionFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            gimnasio.nombre = informacion['nombre']
            gimnasio.apellido = informacion['apellido']
            gimnasio.dni = informacion['dni']
            gimnasio.actividad = informacion['actividad']

            gimnasio.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "paginas/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
      miFormulario = natacionFormulario(initial={'nombre': gimnasio.nombre, 'apellido': gimnasio.apellido,
                                                   'dni': gimnasio.dni, 'actividad': gimnasio.actividad})

    # Voy al html que me permite editar
    return render(request, "paginas/gimnasio.html", {"miFormulario": miFormulario, "natacion_nombre": gimnasio_nombre})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "paginas/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "paginas/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "paginas/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "paginas/login.html", {"form": form})

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"paginas/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"paginas/registro.html" ,  {"form":form})

@login_required
def inicio(request):

    return render(request, "paginas/inicio.html")

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "paginas/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
      
    return render(request, "paginas/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
