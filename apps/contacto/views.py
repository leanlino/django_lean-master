from django.shortcuts import render, redirect

# Create your views here.
def contact(request):
    return render(request, 'pages/contact.html')

def submit(request):
    if request.method == 'POST':
        print(request.POST)
        
        return redirect('home')
    return render(request, 'pages/contact.html')