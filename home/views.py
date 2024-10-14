from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

action_stack = []

def home(request):
    return render(request, 'home.html', {
        'actions':action_stack
    })
    
def perform_action(request):
    if request.method == "POST":
        action = request.POST.get('action_text')
        if action:
            action_stack.append(action)
            messages.success(request, f"Action '{action}' performed successfully!")
        else:
            messages.error(request, "No action text provided!")
    return redirect('home')

def undo_action(request):
    if action_stack:
        last_action = action_stack.pop()
        messages.success(request, f"Action '{last_action}' undone successfully!")
    else:
        messages.error(request, "No action to undo")
    return redirect('home')