from django.shortcuts import render
from .models import Note
from .forms import NoteForm


def notes_list(request):
    notes_list = Note.objects.all()
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.save()
    return render(request, 'notebook.html', {'form': form, 'notes_list': notes_list})

# Create your views here.
