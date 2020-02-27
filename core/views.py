from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PostNote

from .models import Note

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, "pk": pk})

def new_note(request):
    if request.method == "POST":
        form = PostNote(request.POST)
        if form.is_valid():
          form.save()
          return redirect('notes_list')
    else:
        form = PostNote()
    return render(request, 'core/new_note.html', {'form': form})

def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = PostNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_detail', pk=note.pk)
    else:
        form = PostNote(instance=note)
    return render(request, 'core/new_note.html', {'form': form})

def note_delete(request, pk):
  note = get_object_or_404(Note, pk=pk)
  note.delete()
  return redirect('notes_list')