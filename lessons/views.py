from django.shortcuts import render
from .models import Lesson
from trycode.models import TryCode
# from .forms import CodeForm

# Create your views here.
def lessons(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons' : lessons,

    }
    return render(request, 'lessons/lessons.html',context)

import subprocess

def detail(request, pk):
    lessons = Lesson.objects.all()
    lesson = Lesson.objects.get(pk=pk)
    detail_html = "lesson_detail_" + str(lesson.id)
    trycodes = TryCode.objects.filter(in_lesson=lesson)
    if request.method == 'POST':
        code = request.POST.get('code')
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.replace('\n', '<br>')
        else:
            output = result.stderr.replace('\n', '<br>')

    
    context = {
        'lessons' : lessons,
        'lesson' : lesson,
        'trycodes':trycodes,
        # 'form': form,

    }
    return render(request, f'lessons/{detail_html}.html', context)


