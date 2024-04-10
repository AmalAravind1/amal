

from .forms import UserProfileForm
# Create your views here.
from django.shortcuts import render, redirect


def view_profile(request):
    user = request.user
    return render(request,'view.html', {'profile': user})


def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the profile view
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request,'edit1.html', {'form': form})
