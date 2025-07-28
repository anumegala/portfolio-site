from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html") 

def about(request):
    return render(request,"about.html")

def skill(request):
    return render(request,"skill.html")

def project(request):
    project_show=[
        {
            "title":"Menu Page",
            "path":"images/pic1.png"
        },
        {
            "title":"View Order",
            "path":"images/pic2.png" 
        },
        {  
            "title":"GPS Track",
            "path":"images/pic3.png"
        },
        {
            "title":"My Cart",
            "path":"images/pic5.png"
        },
        {
            "title":"Check Out",
            "path":"images/pic6.png"
        },
        {
            "title":"Contact",
            "path":"images/pic4.png"
        }
    ]
    return render(request,"project.html",{"project_show":project_show})

def certificate(request):
    certificates = [
        {'name': 'DPP', 'description': 'Diploma in programing core PYTHON', 'image': 'images/cer1.jpg'},
        {'name': 'PYTHON', 'description': 'Debuging', 'image': 'images/cer2.jpg'},
        {'name': 'ML', 'description': 'Machine Learning with python', 'image': 'images/cer3.jpg'},
        {'name': 'TECHNEX', 'description': 'Chatgpt and Inernet of things(IOT)', 'image': 'images/cer5.jpg'},
        {'name': 'ENTREPRENEURSHIP', 'description': 'National Level youth conclave', 'image': 'images/cer4.jpg'},
    ]
    return render(request, "certificate.html", {'certificate': certificates})

def contact(request):
    return render(request,"contact.html")

def resume(request):
    return render(request, "resume.html")
       
