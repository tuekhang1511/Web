from django.shortcuts import render
from .models import TryCode
from lessons.models import Lesson

import subprocess

def try_code(request, iden):
    lessons = Lesson.objects.all()
    try_code_obj = TryCode.objects.get(identification=iden)
    code = TryCode.objects.get(identification=iden).detail
    result = ''
    output=''
    if request.method == 'POST':
        code = request.POST.get('code')
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.replace('\n', '<br>')
        else:
            output = result.stderr.replace('\n', '<br>')                
    
    context = {
        'lessons':lessons,
        'try_code_obj':try_code_obj,
        'code': code,
        'output': output,
    }
    return render(request, 'trycode/detail.html', context)