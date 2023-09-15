from django.shortcuts import render
from django.http import JsonResponse
from core.models import Cursos

def lista_cursos(request):
    curso = Cursos.objects.get(id_curso = 2)
    response = {'curso':curso}
    return render(request,'IndexCurso.html')


#def criar_curso(request):
 #   if request.method == 'POST':
  #      titulo_curso = request.POST.get('titulo_curso')
   #     url = request.POST.get('url')
    #    qtt_modulos = request.POST.get('qtt_modulos')
     #   categoria = request.POST.get('categoria')
      #  avaliacao = request.POST.get('avaliacao')
       # instrutor = request.POST.get('instrutor')
        #plataforma = request.POST.get('plataforma')

        #curso = Curso(
         #   titulo_curso=titulo_curso,
          #  url=url,
           # qtt_modulos=qtt_modulos,
            #categoria=categoria,
            #avaliacao=avaliacao,
            #instrutor=instrutor,
            #plataforma=plataforma
        #)
        #curso.save()

        #response_data = {'message': 'Curso criado com sucesso!'}
        #return JsonResponse(response_data)
#/////////////////////////////////////////////definir template
    #return render(request, 'seu_template.html')
