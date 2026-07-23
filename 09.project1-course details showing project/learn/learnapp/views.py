from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def courses(request):

    course_list = [

        {
            "name": "Python Programming",
            "duration": "40 Hours",
            "fees": 4999
        },

        {
            "name": "Django Web Development",
            "duration": "35 Hours",
            "fees": 5999
        },

        {
            "name": "Power BI",
            "duration": "30 Hours",
            "fees": 3999
        },

        {
            "name": "Machine Learning",
            "duration": "50 Hours",
            "fees": 7999
        },

        {
            "name": "Data Analytics",
            "duration": "45 Hours",
            "fees": 6999
        }

    ]

    return render(request, "course.html", {"courses": course_list})


def trainers(request):

    trainer_list = [

        {
            "name": "John Mathew",
            "skill": "Python & Django",
            "experience": "6 Years",
            "image": "images/trainer1.jpg"
        },

        {
            "name": "Akhil Raj",
            "skill": "Power BI",
            "experience": "5 Years",
            "image": "images/trainer2.jpg"
        },

        {
            "name": "Anjali S",
            "skill": "Machine Learning",
            "experience": "7 Years",
            "image": "images/trainer3.jpg"
        }

    ]

    return render(request, "trainer.html", {"trainers": trainer_list})


def contact(request):
    return render(request, "contact.html")