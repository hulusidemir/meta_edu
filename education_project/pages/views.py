from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course


# def index(request):
#     courses = Course.objects.filter(
#         is_course_available=True).order_by('-course_date')[:2]
#     context = {
#         'courses': courses,
#     }
#     return render(request, "index.html", context)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['courses'] = Course.objects.filter(is_course_available=True).order_by('-course_date')[:2]
        context['courses'] = Course.objects.filter(is_course_available=True).order_by('-course_date')[:2]
        context['total_course'] = Course.objects.all().count()

        
        return context



class AboutView(TemplateView):
    template_name = "about.html"