from django.contrib import admin
from django import forms

from publications.models import Publication, PublicationLike

from redactor.widgets import RedactorEditor



class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = Publication
        widgets = {
           'body': RedactorEditor(),
        }
        fields = ("title", "body", "image", "author")

class PublicationAdmin(admin.ModelAdmin):
    form = PublicationAdminForm

admin.site.register(Publication, PublicationAdmin)
admin.site.register(PublicationLike)