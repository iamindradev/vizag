from django.http import HttpResponse, HttpRequest, Http404 , JsonResponse
from .models import mark,teacher,login,querytb
import json 
login_data = login.objects.all()
# -------------------------------------------------------------------------------------------------------------------------------
def homepage(request):
    return HttpResponse("hello")


#-----------------------------------------------------------------------------------------------------------------------------------

def loginpage(request):

    if request.method == 'POST':
        
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        username = data["username"]
        password = data["password"]
        print(username)
        for un in login_data:
            if username == un.college_id:
                a=(un.college_id)
                strg=str(un.college_id)
                b=(un.password)
                if password == un.password:
                    if strg[0] == "f":
                        t="welcome teacher"
                        x={
                            "a":a,"b":b,"value":t
                        }
                        
                        break
                    else:
                        t ="welcome student" 
                        student_data=list(teacher.objects.filter(lib=username).values())
                        
                        x={
                            "a":a,"b":student_data,"value":t
                        }
                        
                        break
                else:
                    y="give correct password"
            else:
                t="give correct input" 
                a=(un.college_id)
                b=(un.password)
                x={
                    "a":a,"b":b,"value":t
                }
            
    return JsonResponse(x, safe = False)
          # x="a"
        # uname = login.username
        # passw = login.password


        
        # y="both username and password is wrong"

        # # data=json.loads(request.body)
        # # username = json.JSONDecoder(data)

        # print(type(data))
        
    #     data= hello
    #     print(data)

    
    #     # username=request.POST.get('username')
        # print(username)
#------------------------------------------------------------------------------------------------------------------------------------------
def addstudent(request):
    if request.method =="POST":
    
        body_unicode = request.body.decode('utf-8')
        k = json.loads(body_unicode)
       
        teacher.objects.create(**k)
        r={"data":k,"status":"ok" } 
        y=json.dumps(r)
    return HttpResponse(y)
#----------------------------------------------------------------------------------------------------------------------------------------------
def seedetails(request):
    if request.method == "POST":
        teacher_data = list(teacher.objects.all().values())
    return JsonResponse(teacher_data , safe= False)

#--------------------------------------------------------------------------------------------------------------------------------------
def update(request):
    if request.method =="POST":
        body_unicode = request.body.decode('utf-8')
        k = json.loads(body_unicode)
        username=k['lib_id']
        for i in teacher.objects.all():
            if username ==i.lib_id:    
                teacher.objects.filter(college_id=username).update(**k)
                p= "updated"
            else:
                p= "cant update give right lib id"


    JsonResponse(p, safe= False)
#---------------------------------------------------------------------------------------------------------------------------------------------------
def raisequery(request):
    if request.method=="POST":
        query= json.loads(request.body)
        id=query['lib']
        if teacher.objects.filter(lib=id).value()==id:
            querytb.objects.create(**query)
            querytb.objects.filter(lib=id).update(status='pending')
            print(query)
        else :
            response="enter your lib id"
            
    return JsonResponse(response,safe= False)

#---------------------------------------------------------------------------------------------------------------------------------------------------
def updatequery(request):
    if request.method=="POST":
        add=json.loads(request.body)
        value=add['value']
        if value==update:
            querytb.objects.filter(lib=id).update(status='approved')
            msg="APPROVED"
        else:
            msg="REJECTED"
            
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# def seequery(request):
#     if request.method=="POST":
#         data=json.
def seequery(request):
    if request.method == "POST":
        query_data = list(querytb.objects.all().values())
    return JsonResponse(query_data , safe= False)
        
