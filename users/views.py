from django.shortcuts import render
from imaplib import IMAP4
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def login_user(request):

    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                # Check if this user is valid on the mail server
                c = IMAP4('newmailhost.cc.iitk.ac.in')
                c.login(form.username, form.password)
                return HttpResponse("you have been logged in successully!")
            except:
                return render(request, 'users/login.html', {"form": form})
        else:
            form=AuthenticationForm()
            return render(request, 'users/login.html', {'form': form})

    else:
        form=AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
