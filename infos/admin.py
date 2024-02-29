from django.contrib import admin

from infos.models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = 'nome', 'idade', 'remedios',
