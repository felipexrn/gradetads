from django.shortcuts import render, redirect, get_object_or_404
from .models import Disciplina

def visualizar_grade(request):
    disciplinas = Disciplina.objects.all()
    
    # Organizando disciplinas por período
    disciplinas_por_periodo = {}
    for disciplina in disciplinas:
        if disciplina.periodo not in disciplinas_por_periodo:
            disciplinas_por_periodo[disciplina.periodo] = []
        disciplinas_por_periodo[disciplina.periodo].append(disciplina)

    total_horas_concluidas = sum(disciplina.carga_horaria for disciplina in disciplinas if disciplina.concluida)

    return render(request, 'disciplinas/grade.html', {
        'disciplinas_por_periodo': disciplinas_por_periodo,
        'total_horas_concluidas': total_horas_concluidas,
    })

def marcar_concluida(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    disciplina.concluida = not disciplina.concluida  # Alterna o status
    disciplina.save()
    return redirect('visualizar_grade')

def minha_view(request):
    disciplinas = Disciplina.objects.all()
    total_horas_concluidas = sum(disciplina.carga_horaria for disciplina in disciplinas if disciplina.concluida)
    
    return render(request, 'disciplinas/grade.html', {
        'disciplinas': disciplinas,
        'total_horas_concluidas': total_horas_concluidas,
    })