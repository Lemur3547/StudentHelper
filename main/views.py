from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.mixins import MenuDataMixin
from main.models import Material, Solution, Subject

# Create your views here.


class SubjectListView(ListView):
    model = Subject


class SubjectDetailView(DetailView):
    model = Subject
    slug_field = 'slug'
    slug_url_kwarg = 'subject'


class MaterialDetailView(MenuDataMixin, DetailView):
    model = Material
    slug_field = 'slug'
    slug_url_kwarg = 'material'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["solutions"] = Solution.objects.filter(
            material=self.object).order_by("variant")
        return context
    
    def get_object(self):
        subject_slug = self.kwargs['subject']
        material_slug = self.kwargs['material']
        return Material.objects.get(
            slug=material_slug,
            subject__slug=subject_slug
        )


class SolutionDetailView(MenuDataMixin, DetailView):
    model = Solution
    slug_field = 'slug'
    slug_url_kwarg = 'solution'

    def get_object(self):
        subject_slug = self.kwargs['subject']
        material_slug = self.kwargs['material']
        solution_slug = self.kwargs['solution']
        return Solution.objects.get(
            slug=solution_slug,
            material__slug=material_slug,
            material__subject__slug=subject_slug
        )
