from django.shortcuts import render

# Create your views here.
from app.models import VisitorDeatils
from app.models import UserDetail

def Details(request):
    try:
        userName = request.POST.get("uname")
        Email = request.POST.get("email")
        pw = request.POST.get("PW")
        cpw = request.POST.get("CPW")
        if userName!='' and Email!='' and pw!='' and cpw!='' and pw==cpw:
            UserDetail(userName=userName, Email=Email, pw=pw).save()
            return render(request, "admin.html")
        else:
            return render(request, "UserSignup.html")
    except ValueError:
        return render(request,"UserSignup.html")

def Login(request):
    if request.method == "POST":
        try:
            userName = request.POST.get("name")
            pw = request.POST.get("pw")
            try:
                res = UserDetail.objects.get(Email=userName)
                print(res.Email,res.pw)
                if userName == str(res.Email) and pw == res.pw:
                   return render(request,"user.html")
                else:
                    return render(request, "UserLogin.html", {"msg": "Invalid Customer ID and Password"})
            except UserDetail.DoesNotExist:
                return render(request, "UserLogin.html")
        except ValueError:
            return render(request,"UserLogin.html")

def VisitorData(request):
    if request.method == "POST":
        try:
            username = request.POST.get("name")
            Cname = request.POST.get("Cname")
            Email = request.POST.get("email")
            ContactNo = request.POST.get("ContactNo")
            Date = request.POST.get("date")
            Add = request.POST.get("add")
            city = request.POST.get("City")
            state = request.POST.get("state")
            note = request.POST.get("note")
            VisitorDeatils(UserName=username, Cname=Cname, Email=Email, ContactNo=ContactNo, Date=Date, Address=Add,
                           City=city, State=state, note=note).save()
            return render(request,"user.html")
        except ValueError:
            return render(request, "visitorEntryForm.html")



def checkAdmin(request):
    try:
        name = request.POST.get("name")
        pw = request.POST.get("pw")
        if name == "vijay chawada" and pw == "vijay chawada":
            return render(request,"admin.html")
        else:
            return render(request,"adminLogin.html")
    except ValueError:
        return render(request,"adminLogin.html")


def viewVisitor(request):
    try:
        res = VisitorDeatils.objects.all()
        return render(request,"viewVisitor.html",{"Data":res})
    except:
        return render(request,"user.html")