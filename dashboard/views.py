from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseForbidden

@login_required
def artist_dashboard(request):
    if not request.user.is_superuser:  # or check username/email
        return HttpResponseForbidden()
    return render(request, 'dashboard/dashboard.html')
