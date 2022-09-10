from django.shortcuts import render

# Create your views here.
from library.models import admin_user,books
from library.permission import is_session_active


def index(request):
    return render(request,'home.html')

def login(request):
    if (request.method == 'GET'):
        return render(request, "login.html", {})
    if (request.method == 'POST'):
        username = request.POST["username"]
        password = request.POST["password"]

        eObj = None

        try:
            eObj = admin_user.objects.filter(emailid=username, password=password)
        except:
            return render(request, "login.html", {"msg": "invalid username or password"})

        if (eObj):
            e = eObj.first()
            # keep session data as login is success
            request.session["id"] = e.id
            request.session["fname"] = e.firstname
            request.session["lname"] = e.lastname
            request.session["email"] = e.emailid
            return render(request, "menu.html", {"name":request.session["fname"] +' '+ request.session["lname"]})
        else:
            return render(request, "login.html", {"msg": "invalid username or password"})

def register(request):
    if (request.method == 'GET'):
        return render(request, 'register.html')

    if (request.method == 'POST'):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        emailid = request.POST["email"]
        password = request.POST["password"]
        try:
            admin_user.objects.get(emailid=emailid)
            return render(request, "register.html", {"msg": "User already exists"})
        except:
            e = admin_user(firstname=firstname, lastname=lastname, age=age, emailid=emailid,password=password)
            e.save()
    return render(request, "menu.html", {"msg": " Registration sucess....please login"})

def logout(request):
    if (request.method == 'GET'):
        # delete the session data during the logout
        del request.session["id"]
        del request.session["fname"]
        del request.session["lname"]
    return render(request, "login.html", {"msg": "logout sucess.."})

@is_session_active
def myprofile(request):
    li = admin_user.objects.get(id=request.session['id'])
    return render(request, 'myprofile.html',{'emps':li})

@is_session_active
def getallbooks(request):
    all_books = books.objects.all()
    return render(request, 'allbooks.html',{'books':all_books})

@is_session_active
def addbook(request):
    if (request.method == 'GET'):
        return render(request, 'addbook.html')

    if (request.method == 'POST'):
        title = request.POST["Title"]
        author = request.POST["Author"]
        pages = int(request.POST["Pages"])
        language = request.POST["Language"]
        try:
            books.objects.get(Title=title)
            return render(request, "addbook.html", {"msg": "Book Already exists"})
        except:
            e = books(Title=title, Author=author, Pages=pages, language=language)
            e.save()
    return render(request, "menu.html", {"msg": "Book added successfully."})

@is_session_active
def delete_book(request):
    title = request.GET["title"]
    try:
        eObj = books.objects.get(Title=title)
        eObj.delete()
        return render(request, "getall.html", {"msg": "delete success"})
    except:
        return render(request, "menu.html", {"msg": "Something went wrong"})

@is_session_active
def update_book(request):
    if (request.method == 'GET'):
        book_title = request.GET["title"]
        return render(request, 'updatebook.html', {"title": book_title})

    if (request.method == 'POST'):
        title = request.POST["Title"]
        author = request.POST["Author"]
        pages = request.POST["Pages"]
        language = request.POST["Language"]
        try:
            e = books.objects.get(Title=title)
            print(e.Title)
            e.Title = title
            if author != '':
                e.Author = author
            elif pages != "":
                e.Pages = pages
            elif language != '':
                e.language = language
            e.save()
            return render(request, "allbooks.html", {"msg": "Updated Successfully"})
        except:
            return render(request, "menu.html", {"msg": "Something went wrong"})

