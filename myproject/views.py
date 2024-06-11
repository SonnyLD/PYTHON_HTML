from django.template import Template, Context # type: ignore
from django.http import HttpResponse # type: ignore


import datetime as datetime

def saludar (request):
  saludo = "Bienvenidos a Django"
  return HttpResponse(saludo)

def bienvenidos (request, nombre, apellido):
  saludo = f"Te damos la bienvenida {nombre}, {apellido}"
  return HttpResponse(saludo)

def bienvenidos_html (request, nombre, apellido):
  hoy = datetime.datetime.now()

  saludo = f"""
  <html>
  <h1>Bienvenidos al curso de django!!</h1>
  <h2>Te damos la bienvenida {nombre}, {apellido}</h2>
  <h3>Hoy es {hoy}</h3>
  </html>
  """
  return HttpResponse(saludo)

def bienvenidos_tpl(request):
    ruta_plantilla = "/mnt/c/Users/C12780/Desktop/PY_CHOICE/PYTHON/Clase_17/myproject/myproject/plantillas/bienvenido.html"
    with open(ruta_plantilla) as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)

    return HttpResponse(saludo)