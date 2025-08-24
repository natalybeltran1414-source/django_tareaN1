from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("Hola mundo")

def mostrar_nombres(request):
    return HttpResponse("Nataly Mishel Quisilema Beltran")
def home_page(request):  # <-- Agrega esta función
    return HttpResponse("¡Bienvenido a la página principal!")