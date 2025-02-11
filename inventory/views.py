from django.http import JsonResponse
from .models import inventory, cetegory
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_new(request):
    inventory_name = request.POST.get("name")
    inventory_capacity = request.POST.get("capacity")
    inventory_location = request.POST.get("location")
    personnal_id = request.POST.get("manager")
    inventory_category = request.POST.get("category")
    ctx = {}
    inventory_id = f"{inventory_name}{inventory_capacity}{inventory_location}{personnal_id}{inventory_category}"

    if inventory.objects.filter(inventory_id=inventory_id).exists():
        ctx = {
            'icon': 'info',
            'message': 'انبار از قبل موجود است',
            'success': True
        }
    else:
        inventory.objects.create(
            inventory_id = inventory_id,
            inventory_name = inventory_name,
            inventory_capacity = inventory_capacity,
            inventory_location = inventory_location,
            personnal_id = personnal_id,
            inventory_category = inventory_category
        )
        ctx = {
            'icon': 'success',
            'message': 'انبار ایجاد شد',
            'success': True
        }
    return JsonResponse(ctx)

@csrf_exempt
def inventory_list(request):
    ctx = []
    for i in inventory.objects.all():
        ctx.append(
            {
                'id': i.inventory_id,
                'name': i.inventory_name,
                'category': i.inventory_category,
                'location': i.inventory_location,
                'capacity': i.inventory_capacity,
                'manager': i.personnal_id,

            }
            )
        
        
    return JsonResponse({
        'status': '200',
        'message': ctx,
        'success': True,
    })

@csrf_exempt
def create_new_category(request):
    category_name = request.POST.get("name")
    category_desc = request.POST.get("desc")
    ctx = {}
    category_id = f"{category_name}"

    if cetegory.objects.filter(category_id=category_id).exists():
        ctx = {
            'icon': 'info',
            'message': 'دسته بندی از قبل موجود است',
            'success': True
        }
    else:
        cetegory.objects.create(
            category_id = category_id,
            category_name = category_name,
            category_desc = category_desc,
        )
        ctx = {
            'icon': 'success',
            'message': 'دسته بندی ایجاد شد',
            'success': True
        }
    return JsonResponse(ctx)

@csrf_exempt
def category_list(request):
    ctx = []
    for i in cetegory.objects.all():
        ctx.append(
            {
                'id': i.category_id,
                'name': i.category_name,
                'desc': i.category_desc,
            }
            )
        
        
    return JsonResponse({
        'status': '200',
        'message': ctx,
        'success': True,
    })