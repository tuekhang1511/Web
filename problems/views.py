from django.shortcuts import render
from .models import Problem
from lessons.models import Lesson
from .forms import CodeForm
from .models import Category
from django.db.models import Q

# Create your views here.
# Create your views here.
def problems(request, pk):
    lessons = Lesson.objects.all()
    lesson = Lesson.objects.get(pk=pk)
    problems = Problem.objects.filter(in_lesson=lesson)
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    if category_id:
        problems = problems.filter(category_id=category_id)
    if query:
        problems = problems.filter(Q(name__icontains=query) | Q(problem_description__icontains=query))

    context = {
        'lessons' : lessons,
        'lesson':lesson,
        'problems' : problems,
        'query': query,
        'categories': categories,
    }
    return render(request, 'problems/problems.html',context)

import subprocess

def detail(request, pk, id):
    lessons = Lesson.objects.all()
    lesson = Lesson.objects.get(pk=pk)
    problem = Problem.objects.filter(in_lesson=lesson).get(pk=id)
    word_in_solution_code = problem.word_in_solution_code.split(',')
    code = ''
    result = ''
    output=''
    if request.method == 'POST':
        code = request.POST.get('code')
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.replace('\n', '<br>')
        else:
            output = result.stderr.replace('\n', '<br>')
    print(output.split('<br>'))
    output_text = ''
    count = 0
    output_list = output.split('<br>')
    for element in output_list:
        output_text += element
    if output_text == problem.result:
        for word in word_in_solution_code:
            if word in code:
                count += 1
            if count == len(word_in_solution_code):
                print("Success")
                
    
    context = {
        'problem' : problem,
        'lessons' : lessons,
        # 'form': form,
        'code': code,
        'output': output,
    }
    return render(request, 'problems/detail.html', context)
