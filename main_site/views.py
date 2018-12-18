from django.views.generic import DetailView, TemplateView

from main_site.models import MO


# class AjaxableResponseMixin:
#     def form_invalid(self, form):
#         response = super().form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         if self.request.is_ajax():
#             data = {
#                 'name': self.object.name,
#             }
#             return JsonResponse(data)
#         else:
#             return response


class MOListView(DetailView):
    template_name = 'main_site/mo_view.html'
    model = MO


class HomePage(TemplateView):
    template_name = 'main_site/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            name = self.kwargs['q']
        except:
            name = ''
        if (name != ''):
            mo = MO.objects.filter(name__icontains=name)
        else:
            mo = MO.objects.all()
        context.update({
            'mo': mo,
        })
        return context







    # def get(self, request):
    #     if self.request.is_ajax():
    #         data = {
    #             'name': self.MO.name,
    #         }
    #         return JsonResponse(data)
    #     else:
    #         return HttpResponse(request)










# class MOCatView(TemplateView):
#     template_name = 'main_site/mo_view.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         mo = models.MO.objects.all()
#         photomo = models.PhotoMO.objects.all()
#         context.update({
#             'mo': mo,
#             'photomo': photomo
#         })
#         return context
