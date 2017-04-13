from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from publications.models import Publication, PublicationLike
from publications.forms import PublicationForm


def publications(request):
    form = PublicationForm()
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Publication.objects.create(title=data.get("title"),
                                       body=data.get("body"),
                                       image=data.get("image"),
                                       author=request.user)
    publications = Publication.objects.all()

    paginator = Paginator(publications, 10)
    page = request.GET.get('page')
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)

    return render(request, "publications.html", {"publications": publications,
                                                 "form": form})


def single_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    return render(request, "single_publication.html", {"publication": publication})

def like_single_publication(request, publication_id):
    if request.user.is_authenticated():
        publication = get_object_or_404(Publication, pk=publication_id)
        if PublicationLike.objects.filter(publication=publication, user=request.user).exists():
            PublicationLike.objects.filter(publication=publication, user=request.user).delete()
        else:
            PublicationLike.objects.create(publication=publication, user=request.user)
        return HttpResponseRedirect(reverse("single_publication", kwargs={"publication_id": publication_id}))
    else:
        return HttpResponseRedirect(reverse("login"))