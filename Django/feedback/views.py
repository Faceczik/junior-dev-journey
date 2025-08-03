from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
            name = form.cleaned_data['name'],
            message = form.cleaned_data['message']
            )
            return redirect('home')
    else:
        form = MessageForm()
    
    messages = Message.objects.order_by('-created_at')
    return render(request, 'home.html', {'form': form, 'messages': messages})