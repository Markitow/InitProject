"""
Author :    Marc Taron
Version :   1.0
Name :      AppOne/forms.py
Date :      XX/XX/XX

Docstring : This file define the differents forms of the AppOne
"""
# Do not forget to import forms from django
from django import forms

# Example of list of choice that would be use in form
BOOK_GENRES = [(1, "Roman"), (2, "Science-fiction"), (3, "Fantasy"), (4, "Policier"), (5, "Théâtre"), (6, "Poésie"),
               (7, "Conte"), (8, "Biographie"), (9, "Philosophie"), (10, "Nouvelles")]
SHARED_CHOICES = [(1, "Oui"), (0, "Pas maintenant")]


# Example of a form
class Bookform(forms.Form):
    # max_length should be the same that the one defined in the model
    # required means that blank is ok
    # widget allows to format the field
    title = forms.CharField(label='Title', max_length=256, required=False,
                            widget=forms.TextInput(attrs={'class': 'textinputclass', 'placeholder': 'Titre'}))
    description = forms.CharField(label='Description', required=False,
                                  widget=forms.Textarea(attrs={'class': 'textareaclass txta', 'placeholder': 'Résumé'}))
    genre = forms.MultipleChoiceField(label='Genre', widget=forms.SelectMultiple(attrs={'class': 'item_btn_genre'}),
                                      choices=BOOK_GENRES, required=False)
    shared = forms.ChoiceField(label="Public", widget=forms.RadioSelect(attrs={'class': 'radio_btn_shared'}),
                               choices=SHARED_CHOICES, required=False)
    picture = forms.URLField(label='Picture', widget=forms.FileInput, required=False)

# In views, you will have to import the forms : from [appname].models import Book, Chapter ...
# In views, you will have to initiate the form : form = Bookform()
# In views, you will have to add it to content, to pass it to template : context = {'form': form,}
# In views, when you get the form, you can do :
#     if request.method == "POST":
#         form = Bookform(request.POST)
#         if form.is_valid():
#             # Create new book
#             Book.objects.create(writer=request.user, title=form.cleaned_data['title'],
#                                 description=form.cleaned_data['description'], genre=genre_list,
#                                 picture=form.cleaned_data['picture'], shared=sharing, last_modified=datetime.now())

# In templates, you can call it : {{form.[fieldname]}} or example : {{form.title}}
# In templates, for multiple choice, you can do :
# < div class ="form_item" >
#     < span class ="form_span" > Voulez-vous que ce chapitre puisse être lu par les autres utilisateurs ?
#     < / span > < br / >
#         { % for item in form.shared %}
#             < label for ="{{item.id_for_label}}" class ="form_btn btn_label_shared" >
#                 {{item.choice_label}}
#                 < span class ="shared_item" > {{item.tag}} < / span >
#             < / label >
#         { % endfor %}
# < / div >
