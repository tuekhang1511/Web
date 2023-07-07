from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.models import User
# from .models import EmailVerificationToken
from django.urls import reverse
from problems.models import Problem
from lessons.models import Lesson

# from item.models import Category,Item
# from core.models import User
# from .forms import SignupForm, ChangeAvatarForm

# from .models import user_avatar_upload_path

# Create your views here.
def index(request):
    problems = Problem.objects.all()
    lessons = Lesson.objects.all()
    context = {
        'problems':problems,
        'lessons' : lessons,
    }
    return render(request, 'core/index.html',context)