from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from blog.models import *
from emission.forms import EmissionPodcastCommentForm
from emission.models import *
from music.models import Music
from video.models import Video, Clip


# Create your views here.
class EmissionPodcastHomeView(ListView):
    model = EmissionPodcast
    paginate_by = 12
    template_name = 'emission/podcast/emission_podcast_home.html'

    def get_context_data(self, **kwargs):
        emission_podcast_published = EmissionPodcast.objects.filter(status='published')

        context = super().get_context_data(**kwargs)
        context['emission_podcast_published'] = emission_podcast_published
        return context


class EmissionPodcastDetailView(DetailView):
    model = EmissionPodcast
    template_name = "emission/podcast/emission_podcast_detail.html"

    def get_context_data(self, **kwargs):
        emission_podcast = get_object_or_404(EmissionPodcast, slug=self.kwargs.get('slug'))
        emission_podcast_published = EmissionPodcast.objects.filter(status='published')

        context = super().get_context_data(**kwargs)
        context['emission_podcast_published'] = emission_podcast_published
        context['emission_podcast'] = emission_podcast
        return context
    
    
def emission_podcast_detail(request, slug):
    emission_podcasts = EmissionPodcast.objects.filter(status='published')
    emission_podcast = get_object_or_404(emission_podcasts, slug=slug)
    
    comments = EmissionPodcastComment.objects.filter(emission_podcast=emission_podcast.id)

    new_comment = None
    if request.method == 'POST':
        comment_form = EmissionPodcastCommentForm(data=request.POST)
        if comment_form.is_valid():
            body = comment_form.cleaned_data['body']
            new_comment = comment_form.save(commit=False)
            new_comment.emission_podcast = emission_podcast
            new_comment.author = request.user
            new_comment.save()
            return redirect(emission_podcast.get_absolute_url())
    else:
        comment_form = EmissionPodcastCommentForm()
        
    context = {
        'emission_podcast': emission_podcast,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
               
    return render(request, 'emission/podcast/emission_podcast_detail.html', context)