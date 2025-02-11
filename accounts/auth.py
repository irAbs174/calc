from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    Username = request.POST.get("username")
    password = request.POST.get("password")

    if Username == '' and password =='':
        ctx = {
        'status': '200',
        'message': "../dashboard/dashboard.html",
        'suceess': True
    }
    else:
        ctx = {
        'status': '403',
        'message': "نام کاربری یا رمز عبور صحیح نیست",
        'suceess': False
    }
    
    print(Username, password)
    return JsonResponse(ctx)