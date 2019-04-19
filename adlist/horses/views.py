from horses.models import Horse, Comment

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


from horses.util import HorsesListView, HorsesDetailView, HorsesCreateView, HorsesUpdateView, HorsesDeleteView
from horses.forms import CreateForm, CommentForm

# Create your views here.
class HorseListView(HorsesListView):
    model = Horse
    template_name = 'horses/horse_list.html'

    def get(self, request) :
        horse_list = Horse.objects.all()
        ctx = {'horse_list' : horse_list}
        return render(request, self.template_name, ctx)


class HorseDetailView(HorsesDetailView):
    model = Horse
    template_name = 'horses/horse_detail.html'
    def get(self, request, pk) :
        horse = Horse.objects.get(id=pk)
        comments = Comment.objects.filter(horse=horse).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'horse' : horse, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class HorseCreateView(HorsesCreateView):
    model = Horse
    fields = {'name', 'detail', 'mileage'}
    template_name = 'horses/horse_form.html'

class HorseUpdateView(HorsesUpdateView):
    model = Horse
    fields = ['name', 'detail', 'mileage']
    template_name = 'horses/horse_form.html'

class HorseDeleteView(HorsesDeleteView):
    model = Horse
    template_name = 'horses/horse_delete.html'

class HorseFormView(LoginRequiredMixin, View):
    template = 'horses/horse_form.html'
    success_url = reverse_lazy('horses')
    def get(self, request, pk=None) :
        if not pk :
            form = CreateForm()
        else:
            horse = get_object_or_404(Horse, id=pk, owner=self.request.user)
            form = CreateForm(instance=horse)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            horse = get_object_or_404(Horse, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=horse)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model owner before saving
        horse = form.save(commit=False)
        horse.owner = self.request.user
        horse.save()
        return redirect(self.success_url)

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        horse = get_object_or_404(Horse, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, horse=horse)
        comment.save()
        return redirect(reverse_lazy('horse_detail', args=[pk]))

class CommentDeleteView(HorseDeleteView):
    model = Comment
    template_name = 'horses/comment_delete.html'

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        horse = self.object.horse
        return reverse_lazy('horse_detail', args=[horse.id])
