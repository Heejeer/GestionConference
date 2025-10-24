from django.shortcuts import render,redirect
from .forms import UserForm
def register(req):
    if req.method=="POST":
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=UserForm()
        return render (req,'register.html',{"form":form})
    