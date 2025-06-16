from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Предмет')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Material(models.Model):
    class MaterialType(models.TextChoices):
        LAB = 'laba', 'Лабораторная работа'
        INDEP = 'independent ', 'Самостоятельная работа'
        LECTURE = 'lecture', 'Лекция'

    name = models.CharField(max_length=100, verbose_name='Материал')
    slug = models.SlugField(max_length=100)
    subject = models.ForeignKey('main.Subject', on_delete=models.CASCADE, verbose_name='Предмет')
    type = models.CharField(max_length=15, choices=MaterialType, verbose_name='Тип материала')
    content = models.JSONField(verbose_name='Условие')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

class Solution(models.Model):
    slug = models.SlugField(max_length=100)
    material = models.ForeignKey('main.Material', on_delete=models.CASCADE, verbose_name='Материал')
    variant = models.PositiveSmallIntegerField(verbose_name='Вариант')
    content = models.JSONField(verbose_name='Решение')

    def __str__(self):
        if self.variant != 0:
            return f'Решение {self.material.name} вариант {self.variant}'
        else:
            return f'Решение {self.material.name}'
    
    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'