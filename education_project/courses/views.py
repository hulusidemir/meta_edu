from django.shortcuts import render
from .models import Category, Course, Tag


def course_list(request):
    courses = Course.objects.all().order_by('-course_date')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories
    }
    return render(request, "courses.html", context)


def course_detail(request, category_slug, course_id):
    course = Course.objects.get(course_category__slug=category_slug, id=course_id)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {
        'course': course,
        'tags': tags,
        'categories': categories
    }
    return render(request, "course_detail.html", context)


def category_list(request, category_slug):
    courses = Course.objects.all().filter(course_category__slug=category_slug)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories
    }
    return render(request, "category_list.html", context)


def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(course_tags__slug=tag_slug)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories
    }
    return render(request, "tag_list.html", context)
