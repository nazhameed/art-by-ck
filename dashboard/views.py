from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import GalleryImage, AvailableArt, JournalEntry
from .forms import GalleryImageForm, AvailableArtForm, JournalEntryForm

@login_required
def artist_dashboard(request):
    if not request.user.is_superuser:  # or check username/email
        return HttpResponseForbidden()
    images = GalleryImage.objects.all().order_by('-created_at')
    available_arts = AvailableArt.objects.all().order_by('-created_at')
    journal_entries = JournalEntry.objects.all().order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {
        'images': images,
        'available_arts': available_arts,
        'journal_entries': journal_entries,
    })

@login_required
def gallery_add(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist_dashboard')
    else:
        form = GalleryImageForm()
    return render(request, 'dashboard/gallery_form.html', {'form': form, 'action': 'Add'})

@login_required
def gallery_edit(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('artist_dashboard')
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'dashboard/gallery_form.html', {'form': form, 'action': 'Edit'})

@login_required
def gallery_delete(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('artist_dashboard')
    return render(request, 'dashboard/gallery_confirm_delete.html', {'image': image})

@login_required
def available_art_add(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = AvailableArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist_dashboard')
    else:
        form = AvailableArtForm()
    return render(request, 'dashboard/available_art_form.html', {'form': form, 'action': 'Add'})

@login_required
def available_art_edit(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    art = get_object_or_404(AvailableArt, pk=pk)
    if request.method == 'POST':
        form = AvailableArtForm(request.POST, request.FILES, instance=art)
        if form.is_valid():
            form.save()
            return redirect('artist_dashboard')
    else:
        form = AvailableArtForm(instance=art)
    return render(request, 'dashboard/available_art_form.html', {'form': form, 'action': 'Edit'})

@login_required
def available_art_delete(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    art = get_object_or_404(AvailableArt, pk=pk)
    if request.method == 'POST':
        art.delete()
        return redirect('artist_dashboard')
    return render(request, 'dashboard/available_art_confirm_delete.html', {'art': art})

@login_required
def journal_add(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist_dashboard')
    else:
        form = JournalEntryForm()
    return render(request, 'dashboard/journal_form.html', {'form': form, 'action': 'Add'})

@login_required
def journal_edit(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    entry = get_object_or_404(JournalEntry, pk=pk)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('artist_dashboard')
    else:
        form = JournalEntryForm(instance=entry)
    return render(request, 'dashboard/journal_form.html', {'form': form, 'action': 'Edit'})

@login_required
def journal_delete(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    entry = get_object_or_404(JournalEntry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('artist_dashboard')
    return render(request, 'dashboard/journal_confirm_delete.html', {'entry': entry})
