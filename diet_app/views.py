from django.shortcuts import render, HttpResponse
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


login_done = 0

name = ""
email = ""
password = ""
age = 0
gender = ""
weight = 0
height = 0
dietary_preferences = ""
allergies = ""
health_goals = ""
phone = ""
# myapp/views.py
from django.shortcuts import redirect
from .models import Register


def register(request):
    if request.method == "POST":
        # Process form submission
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        dietary_preferences = request.POST.get("dietary_preferences", "")
        allergies = request.POST.get("allergies", "")
        health_goals = request.POST.get("health_goals", "")
        phone = request.POST.get("phone", "")
        button = request.POST.get("submit_btn")

        if button == "register":
            # Check if email already exists
            if Register.objects.filter(email=email).exists():
                return render(
                    request,
                    "unauthorized.html",
                    {"error_message": "User already Exists..."},
                )
            else:
                # Create a new Register object and save it to the database
                register_entry = Register(
                    name=name,
                    email=email,
                    password=password,
                    age=age,
                    gender=gender,
                    weight=weight,
                    height=height,
                    dietary_preferences=dietary_preferences,
                    allergies=allergies,
                    health_goals=health_goals,
                )
                register_entry.save()

                name = name
                email = email
                password = password
                age = age
                gender = gender
                weight = weight
                height = height
                dietary_preferences = dietary_preferences
                allergies = allergies
                health_goals = health_goals
                phone = phone

                login_done = 1

                return render(
                    request,
                    "index.html",
                    {"success_message": "Registration Done! Now You can Login."},
                )

    return render(request, "register.html")


# diet plans
from .p1 import *


from django.shortcuts import render
from .models import Register  # Import your Register model


def nut(request):
    return render(request, "nut.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        registrations = Register.objects.filter(email=email, password=password).values()
        registrations = (
            registrations.first()
        )  # Assuming you want the first matching object

        if registrations:

            id = registrations["id"]
            name = registrations["name"]
            email = registrations["email"]
            password = registrations["password"]
            age = registrations["age"]
            gender = registrations["gender"]
            weight = registrations["weight"]
            height = registrations["height"]
            dietary_preferences = registrations["dietary_preferences"]
            allergies = registrations["allergies"]
            health_goals = registrations["health_goals"]
            phone = registrations["phone"]

            print(id, name, email, age)
        else:
            return render(
                request, "index.html", {"error_message": "Invalid email or password."}
            )

    # Render the login form initially
    return render(request, "login.html")


def diet_plan(request):
    registrations = Register.objects.all()
    # registration = Register.objects.get(name=email, email=my_email)
    # if registration:
    #     pass

    return render(request, "diet_plan.html")
