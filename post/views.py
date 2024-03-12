from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
  posts = Post.objects.all()
  for obj in posts:
    print(obj.titulo)
  return HttpResponse('lista de posts')

def storage(request, titulo, cuerpo):
  #creamos la instancia
  post = Post(titulo=titulo, cuerpo=cuerpo)
  post.save()
  #trabajar con el modelo
  return HttpResponse('guardamos en el modelo, no mostramos en la vista')

#metodo para buscar por id
def consultar(request, id):
  post = Post.objects.get(id=id)
  return HttpResponse(f"Titulo: {post.titulo}, Cuerpo: {post.cuerpo}, fecha: {post.fecha}")

#método para modificar
def modificar(request, titulo, id):
  post = Post.objects.get(id=id)
  post.titulo = titulo
  post.save()
  return HttpResponse("Post actualizado")

#metodo para eliminar
def eliminar(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return HttpResponse("Post eliminado")

def consultas(request):
  #Obtener todos los elementos de los post
  posts = Post.objects.all()

  #Filtrar la consulta por una condición
  filtro = Post.objects.filter(titulo='titulo')

  # Obtener un unico registro
  post = Post.objects.get(id= 12)

  # Obtener los 20 primeros elementos
  limite = Post.objects.all()[:20]

  # Obtener los 5 primeros resultados partiendo del item 15
  limite = Post.objects.all()[2:8]

  # Obtener los registros ordenados por el titulo
  orden = Post.objects.all().order_by('-cuerpo')[:20]

  # Obtener los elementos que su id sea menor o igual que 20

  menor = Post.objects.filter(id__lte=20)

  return render(request, 'index.html', {
    'posts': posts,
    'filtro': filtro,
    'post': post,
    'limite': limite,
    'orden' : orden,
    'menor': menor
  })
  #return HttpResponse('consultas')