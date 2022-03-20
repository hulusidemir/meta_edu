from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Teacher

# def teachers(request):
#     teachers = Teacher.objects.all()
    
#     context = {
#         teachers : 'teachers'
#     }
    
#     return render(request, 'teachers.html', context)


# class TeachersView(TemplateView):
#     template_name = "teachers.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["teachers"] = Teacher.objects.all()
        
#         return context


class TeachersView(ListView):
    model = Teacher
    template_name = "teachers.html"
    context_object_name = "teachers"

