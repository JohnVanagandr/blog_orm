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