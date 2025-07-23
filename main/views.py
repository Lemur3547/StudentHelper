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

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        labs = Material.objects.filter(subject=self.object, type='laba')
        for lab in labs:
            lab.materials_count = lab.solution_set.values('variant').distinct().count()
            lab.solutions_count = lab.solution_set.count()

        independents = Material.objects.filter(subject=self.object, type='independent')
        for independent in independents:
            independent.materials_count = independent.solution_set.values('variant').distinct().count()
            independent.solutions_count = independent.solution_set.count()

        context["labs"] = labs
        context["independents"] = independents

        return context


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
