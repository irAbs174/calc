from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def add_personal(request):
    personnal_first_name = request.POST.get("personnal_first_name")
    personnal_last_name = request.POST.get("personnal_last_name")
    personnal_email = request.POST.get("personnal_email")
    personnal_phone_number = request.POST.get("personnal_phone_number")
    personnal_position = request.POST.get("personnal_position")
    personnal_department_id = request.POST.get("personnal_department")
    personnal_date_hired = request.POST.get("personnal_date_hired")
    personnal_type_status = request.POST.get("personnal_type_status")
    personnal_salary = request.POST.get("personnal_salary")
    personnal_address = request.POST.get("personnal_address")
    personnal_melli_code = request.POST.get("personnal_melli_code")
    personnal_birth_date = request.POST.get("personnal_birth_date")
    personnal_emergency_contact = request.POST.get("personnal_emergency_contact")
    
    ctx = {}
    personal_id = f"{personnal_first_name}_{personnal_last_name}&{personnal_melli_code}"
    if CorporatePersonnel.objects.filter(personnal_email=personnal_email).exists():
        ctx = {
            'icon': 'info',
            'message': 'پرسنل با این ایمیل از قبل موجود است',
            'success': False
        }
    else:
        department = Department.objects.get(id=personnal_department_id)
        CorporatePersonnel.objects.create(
            personal_id = personnal_melli_code,
            personnal_first_name=personnal_first_name,
            personnal_last_name=personnal_last_name,
            personnal_email=personnal_email,
            personnal_phone_number=personnal_phone_number,
            personnal_position=personnal_position,
            personnal_department=department,
            personnal_date_hired=personnal_date_hired,
            personnal_type_status=personnal_type_status,
            personnal_salary=personnal_salary,
            personnal_address=personnal_address,
            personnal_melli_code=personnal_melli_code,
            personnal_birth_date=personnal_birth_date,
            personnal_emergency_contact=personnal_emergency_contact
        )
        ctx = {
            'icon': 'success',
            'message': 'پرسنل ایجاد شد',
            'success': True
        }
    return JsonResponse(ctx)

@csrf_exempt
def personal_list(request):
    ctx = []
    for personnel in CorporatePersonnel.objects.all():
        ctx.append(
            {
                'id': personnel.personal_id,
                'first_name': personnel.personnal_first_name,
                'last_name': personnel.personnal_last_name,
                'email': personnel.personnal_email,
                'phone_number': personnel.personnal_phone_number,
                'position': personnel.personnal_position,
                'department': personnel.personnal_department_id,
                'date_hired': personnel.personnal_date_hired,
                'type_status': personnel.personnal_type_status,
                'salary': personnel.personnal_salary,
                'address': personnel.personnal_address,
                'national_code': personnel.personnal_melli_code,
                'emergency_contact': personnel.personnal_emergency_contact,
            }
        )
    return JsonResponse({
        'status': '200',
        'message': ctx,
        'success': True,
    })

@csrf_exempt
def create_department(request):
    department_name = request.POST.get("department_name")
    description = request.POST.get("description")
    ctx = {}
    department_id = f"{department_name}"
    if Department.objects.filter(department_name=department_name).exists():
        ctx = {
            'icon': 'info',
            'message': 'بخش از قبل موجود است',
            'success': False
        }
    else:
        Department.objects.create(
            department_id = department_id,
            department_name=department_name,
            description=description
        )
        ctx = {
            'icon': 'success',
            'message': 'بخش ایجاد شد',
            'success': True
        }
    return JsonResponse(ctx)

@csrf_exempt
def department_list(request):
    ctx = []
    for department in Department.objects.all():
        ctx.append(
            {
                'id': department.department_id,
                'department_name': department.department_name,
                'description': department.description,
            }
        )
    return JsonResponse({
        'status': '200',
        'message': ctx,
        'success': True,
    })