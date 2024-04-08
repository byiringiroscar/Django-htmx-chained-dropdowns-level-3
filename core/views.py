from django.shortcuts import render
from core.models import Course, Module, Tutor

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'university.html', context)


def modules(request):
    course = request.GET.get('course')
    modules = Module.objects.filter(course=course)
    context = {'modules': modules, 'is_htmx': True}
    return render(request, 'partials/modules.html', context)


def tutors(request):
    module = request.GET.get('module')
    tutors = Tutor.objects.filter(module=module)
    context = {'tutors': tutors}
    return render(request, 'partials/tutors.html', context)