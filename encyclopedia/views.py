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
            query = form.cleaned_data["query"]
    content = util.get_entry(query.lower())
    print(content)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": query.lower(),
            "entry_content": markdown(content)
        })
    else:
        entries = util.search_fragment_in_listentries()
        if entries:
            return render(request, "encyclopedia/results.html", {
                "entry_name": f"Search Results for {query}",
                "entry_content": entries
            })
        else:
            return render(request, "encyclopedia/results.html", {
                "entry_name": f"No Search Results for {query}",
                "entry_content": None
            })
