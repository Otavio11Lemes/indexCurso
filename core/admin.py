from django.contrib import admin
from core.models import Cursos
# Register your models here.

class CursoAdmin (admin.ModelAdmin):
    list_display = ('titulo_curso' ,'categoria', 'id_curso')
    list_filter = ('titulo_curso', 'categoria')

admin.site.register(Cursos, CursoAdmin)