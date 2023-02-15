from django.shortcuts import render
from markdown2 import markdown
from django import forms

from . import util


class SearchForm(forms.Form):
    query = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "form": SearchForm(),
        "entries": util.list_entries()
    })


def entry(request, entry_name):
    content = util.get_entry(entry_name)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": entry_name.lower(),
            "entry_content": markdown(content)
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": entry_name.lower(),
            "entry_content": None
        })


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["query"]

    if content:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": entry_name.lower(),
            "entry_content": markdown(content)
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": entry_name.lower(),
            "entry_content": None
        })
