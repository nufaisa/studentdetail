from django.shortcuts import render,redirect
from .models import marklist
from .forms import StudentForm
# Create your views here.
def emp(request):
   if request.method == "POST":
      form = StudentForm(request.POST)
      if form.is_valid():
         try:
            form.save()
            return redirect('/show')
         except:
            pass
   else:
       form = StudentForm
   return render(request, 'index.html', {'form': form})
def show(request):
    marklists = marklist.objects.all()
    return render(request,"show.html",{'marklists':marklists})
def edit(request, id):
    marklis = marklist.objects.get(id=id)
    return render(request,'edit.html', {'marklist':marklis})
def update(request, id):
    marklis = marklist.objects.get(id=id)
    form = StudentForm(request.POST, instance = marklis)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'marklist': marklist})
def destroy(request, id):
     employee = marklist.objects.get(id=id)
     employee.delete()
     return redirect("/show")
