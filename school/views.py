from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

def homepage (req):
    form = StudentForm(req.POST or None)
    data = {
        "students" : Student.objects.all(),
        "form" : form
    }
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)

    return render(req, "index.html", {"form": form, "students": Student.objects.all()})

# Create your views here.
def deleteStudent(req,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect(homepage)

def editStudent(req, id):
    student = Student.objects.get(pk=id)
    form = StudentForm(req.POST or None ,instance=student)

    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    return render(req, "edit.html", {"form": form})


def searchStudent(req):
    if req.method == "GET":
        search_query = req.GET.get("search")
        form = StudentForm()
        # cont
        data = {
            "students" : Student.objects.filter(name__icontains=search_query),
            "form" : form

        }
        return render(req, "index.html",data)


def filterCity(r):
    if r.method == "GET":
        search = r.GET.get("city")
        form = StudentForm()
        data = {
            "form": form,
            "students": Student.objects.filter(city=search)
        
        }
        return  render(r, "index.html",data)


