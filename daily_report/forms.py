from django import forms

from snippets.models import Article


class SnippetForm(Article.ModelForm):
    class Meta:
        model = Article
        fields = ('day', 'name')
