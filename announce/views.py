from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Announce
from .forms import AnnounceForm


class AnnounceDetail(DetailView):
    template_name = 'announces/announce_detail.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs['id']
        return get_object_or_404(Announce, id=id_)


class AnnounceCreate(CreateView):
    template_name = 'announces/announce_create.html'
    form_class = AnnounceForm
    model = Announce

    def get_success_url(self):
        return reverse('announce:announce-list')


class AnnounceUpdate(UpdateView):
    template_name = 'announces/announce_create.html'
    form_class = AnnounceForm
    model = Announce

    def get_object(self, queryset=None):
        id_ = self.kwargs['id']
        return get_object_or_404(Announce, id=id_)

    def get_success_url(self):
        return reverse('announce:announce-list')


class AnnounceList(ListView):
    template_name = 'announces/announce_list.html'
    model = Announce

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Announce, id=request.POST['id'])
        obj.delete()
        return redirect(reverse('announce:announce-list'))

    def get_object(self, queryset=None):
        id_ = self.kwargs['id']
        return get_object_or_404(Announce, id=id_)


class AnnounceDelete(DeleteView):
    template_name = 'announces/announce_delete.html'
    model = Announce

    def get_object(self, queryset=None):
        id_ = self.kwargs['id']
        return get_object_or_404(Announce, id=id_)

    def get_success_url(self):
        return reverse('announce:announce-list')
