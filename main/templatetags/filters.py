from django import template

register = template.Library()


@register.filter
def correct_word_form(value: int, forms: str):
    forms = forms.split(";")
    if 10 < value % 100 < 15:
        return f"{value} {forms[2]}"
    elif value % 10 == 1:
        return f"{value} {forms[0]}"
    elif 1 < value % 10 < 5:
        return f"{value} {forms[1]}"
    else:
        return f"{value} {forms[2]}"
