class MenuDataMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        obj = getattr(self, 'object', None)
        subject = None

        # со страницы решения
        if hasattr(obj, 'material'):
            subject = obj.material.subject
            current_page_slug = obj.material.slug
        # со страницы материала
        elif hasattr(obj, 'subject'):
            subject = obj.subject
            current_page_slug = obj.slug

        if subject:
            labs = subject.material_set.filter(type='laba')
            independents = subject.material_set.filter(type='independent')
            lectures = subject.material_set.filter(type='lecture')
            context['subject'] = subject
            context['labs'] = labs
            context['independents'] = independents
            context['lectures'] = lectures
            context['current_page_slug'] = current_page_slug
        return context