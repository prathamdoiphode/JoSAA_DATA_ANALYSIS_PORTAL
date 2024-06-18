from django.shortcuts import render
from django.http import JsonResponse
from .models import josaaTable
from django.db.models import F
from django.views.decorators.http import require_GET

# for headers function ....
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contributors(request):
    return render(request,'contributors.html')


# for questions function ....
def roundwise(request):
    return render(request,'roundwise.html')

def bestcourse(request):
    return render(request,'bestcourse.html')

def yearwise(request):
    return render(request,'yearwise.html')

def CourseComparison(request):
    return render(request,'CourseComparison.html')

def BestCollege(request):
    return render(request,'BestCollege.html')

def categorywise(request):
    return render(request,'categorywise.html')


# for dropdown data function ....
def get_InstTypewise_Instname(request):
    instype = request.GET.get('instype')
    if instype == 'IIT':
        data = josaaTable.objects.filter(
            Institute__startswith = instype
        ).order_by('Institute').values('Institute').distinct()
    elif instype in ['NIT', 'IIIT']:
        data = josaaTable.objects.filter(
            Institute__icontains = instype
        ).order_by('Institute').values('Institute').distinct()
    else:
        data = josaaTable.objects.exclude(
            Institute__icontains='IIT'
        ).exclude(
            Institute__icontains='NIT'
        ).exclude(
            Institute__icontains='IIIT'
        ).order_by('Institute').values('Institute').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_InstNameWise_ProgrammeName(request):
    institute = request.GET.get('institute')
    data = josaaTable.objects.filter(
            Institute = institute
        ).values('Programme').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_Programmewise_Course(request):
    institute = request.GET.get('institute')
    programme=request.GET.get('programme')
    data = josaaTable.objects.filter(
            Programme=programme,
            Institute = institute
        ).values('Course').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_Coursewise_Category(request):
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    institute=request.GET.get('institute')
    data = josaaTable.objects.filter(
            Course=course,
            Programme=programme,
            Institute = institute
        ).values('Category').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_Categorywise_Gender(request):
    category=request.GET.get('category')
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    institute=request.GET.get('institute')
    data = josaaTable.objects.filter(
            Category=category,
            Course=course,
            Programme=programme,
            Institute = institute
        ).values('Gender').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_RoundDropdown(request):
    data = [{'Round':1},{'Round':2},{'Round':3},{'Round':4},{'Round':5},{'Round':6}]
    return JsonResponse(data, safe=False)

def get_YearDropdown(request):
    data = [{'Year':2016},{'Year':2017},{'Year':2018},{'Year':2019},{'Year':2020},
            {'Year':2021},{'Year':2022},{'Year':2023}]
    return JsonResponse(data, safe=False)

def get_only_Categorywise_Gender(request):
    category=request.GET.get('category')
    data = josaaTable.objects.filter(
            Category=category
        ).values('Gender').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_InstTypeWise_ProgrammeName(request):
    instype = request.GET.get('instype')
    if instype == 'IIT':
        data = josaaTable.objects.filter(
            Institute__startswith = instype
        ).order_by('Programme').values('Programme').distinct()
    elif instype in ['NIT', 'IIIT']:
        data = josaaTable.objects.filter(
            Institute__icontains = instype
        ).order_by('Programme').values('Programme').distinct()
    else:
        data = josaaTable.objects.exclude(
            Institute__icontains='IIT'
        ).exclude(
            Institute__icontains='NIT'
        ).exclude(
            Institute__icontains='IIIT'
        ).order_by('Programme').values('Programme').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_only_Programmewise_Course(request):
    programme=request.GET.get('programme')
    instype=request.GET.get('instype')
    if instype == 'IIT':
        data = josaaTable.objects.filter(
            Institute__startswith = instype,
            Programme=programme
        ).order_by('Course').values('Course').distinct()
    elif instype in ['NIT', 'IIIT']:
        data = josaaTable.objects.filter(
            Institute__icontains = instype,
            Programme=programme
        ).order_by('Course').values('Course').distinct()
    else:
        data = josaaTable.objects.exclude(
            Institute__icontains='IIT'
        ).exclude(
            Institute__icontains='NIT'
        ).exclude(
            Institute__icontains='IIIT'
        ).filter(
            Programme=programme
        ).order_by('Course').values('Course').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_Instype_Coursewise_Category(request):
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    instype=request.GET.get('instype')
    if instype == 'IIT':
        data = josaaTable.objects.filter(
            Institute__startswith = instype,
            Programme=programme,
            Course=course
        ).order_by('Category').values('Category').distinct()
    elif instype in ['NIT', 'IIIT']:
        data = josaaTable.objects.filter(
            Institute__icontains = instype,
            Programme=programme,
            Course=course
        ).order_by('Category').values('Category').distinct()
    else:
        data = josaaTable.objects.exclude(
            Institute__icontains='IIT'
        ).exclude(
            Institute__icontains='NIT'
        ).exclude(
            Institute__icontains='IIIT'
        ).filter(
            Programme=programme,
            Course=course
        ).order_by('Category').values('Category').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_InsType_Categorywise_Gender(request):
    category=request.GET.get('category')
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    instype=request.GET.get('instype')
    if instype == 'IIT':
        data = josaaTable.objects.filter(
            Institute__startswith = instype,
            Programme=programme,
            Course=course,
            Category=category
        ).order_by('Gender').values('Gender').distinct()
    elif instype in ['NIT', 'IIIT']:
        data = josaaTable.objects.filter(
            Institute__icontains = instype,
            Programme=programme,
            Course=course,
            Category=category
        ).order_by('Gender').values('Gender').distinct()
    else:
        data = josaaTable.objects.exclude(
            Institute__icontains='IIT'
        ).exclude(
            Institute__icontains='NIT'
        ).exclude(
            Institute__icontains='IIIT'
        ).filter(
            Programme=programme,
            Course=course,
            Category=category
        ).order_by('Gender').values('Gender').distinct()

    data = list(data)
    return JsonResponse(data, safe=False)

def get_Coursewise_Gender(request):
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    institute=request.GET.get('institute')
    data = josaaTable.objects.filter(
            Course=course,
            Programme=programme,
            Institute = institute
        ).values('Gender').distinct()
    data = list(data)
    return JsonResponse(data, safe=False)




# for table show function ....
def get_Yearwise_Rank_Table(request):
    round=request.GET.get('round')
    gender=request.GET.get('gender')
    category=request.GET.get('category')
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    institute=request.GET.get('institute')
    data = josaaTable.objects.filter(
            Round=round,
            Gender=gender,
            Category=category,
            Course=course,
            Programme=programme,
            Institute = institute
        ).values()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_Roundwise_Rank_Table(request):
    year=request.GET.get('year')
    gender=request.GET.get('gender')
    category=request.GET.get('category')
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    institute=request.GET.get('institute')
    data = josaaTable.objects.filter(
            Year=year,
            Gender=gender,
            Category=category,
            Course=course,
            Programme=programme,
            Institute = institute
        ).values()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_Bestcourse_Table(request):
    category=request.GET.get('category')
    gender=request.GET.get('gender')
    examtype=request.GET.get('examtype')
    rank=request.GET.get('rank')

    if examtype == 'JEE-Advance':
        data = josaaTable.objects.filter(
            Institute__startswith = 'IIT',
            Category=category,
            Gender=gender,
            Closing_Rank__gte=rank,
            Year=2023,
            Round=6
        ).order_by('Opening_Rank','Closing_Rank')[:20].values()
    else:
        data = josaaTable.objects.exclude(
            Institute__startswith = 'IIT'
        ).filter(
            Category=category,
            Gender=gender,
            Closing_Rank__gte=rank,
            Year=2023,
            Round=6
        ).order_by('Opening_Rank','Closing_Rank')[:20].values()
    data = list(data)
    return JsonResponse(data, safe=False)

def get_InstituteWise_Table(request):
    year=request.GET.get('year')
    gender=request.GET.get('gender')
    category=request.GET.get('category')
    course=request.GET.get('course')
    programme=request.GET.get('programme')
    instype=request.GET.get('instype')
    if instype == 'IIT':
        data = josaaTable.objects.filter(
            Institute__startswith = instype,
            Programme=programme,
            Course=course,
            Category=category,
            Gender=gender,
            Year=year,
            Round=1
        ).order_by('Closing_Rank')[:20].values('Institute')
    elif instype in ['NIT', 'IIIT']:
        data = josaaTable.objects.filter(
            Institute__icontains = instype,
            Programme=programme,
            Course=course,
            Category=category,
            Gender=gender,
            Year=year,
            Round=1
        ).order_by('Closing_Rank')[:20].values('Institute')
    else:
        data = josaaTable.objects.exclude(
            Institute__icontains='IIT'
        ).exclude(
            Institute__icontains='NIT'
        ).exclude(
            Institute__icontains='IIIT'
        ).filter(
            Programme=programme,
            Course=course,
            Category=category,
            Gender=gender,
            Year=year,
            Round=1
        ).order_by('Closing_Rank')[:20].values('Institute')
    data = list(data)
    return JsonResponse(data, safe=False)

# for graph show function ....
def get_graph_CategoryWise(request):
    gender = request.GET.get('gender')
    year_value = request.GET.get('year')
    institute = request.GET.get('institute')
    course = request.GET.get('course')
    programname = request.GET.get('programme')
    category=request.GET.get('category')
    round=request.GET.get('round')
    if category == 'PwD':
        data = josaaTable.objects.filter(
            Gender=gender,
            Institute = institute,
            Course = course,
            Year=year_value,
            Round=round,
            Programme = programname,
            Category__icontains = category
        ).values()
    else:
        data = josaaTable.objects.exclude(
            Category__icontains='PwD'
        ).filter(
            Gender=gender,
            Institute = institute,
            Course = course,
            Year=year_value,
            Round=round,
            Programme = programname,
        ).values()

    data = list(data)
    return JsonResponse(data, safe=False)


def get_graph_A_RankWise(request):
    gen_value = request.GET.get('gender_A')
    year_value = request.GET.get('year_A')
    iit_value = request.GET.get('institute_A')
    programtype_value = request.GET.get('course_A')
    programname_value = request.GET.get('programme_A')
    category_value=request.GET.get('category_A')
    data_A = josaaTable.objects.filter(
        
        Category = category_value,
        Gender=gen_value,
        Institute = iit_value,
        Course = programtype_value,
        Programme = programname_value,
        Year=year_value
    ).values()
    data_A = list(data_A)

    return JsonResponse(data_A, safe=False)

def get_graph_B_RankWise(request):
    gen_value = request.GET.get('gender_B')
    year_value = request.GET.get('year_B')
    iit_value = request.GET.get('institute_B')
    programtype_value = request.GET.get('course_B')
    programname_value = request.GET.get('programme_B')
    category_value=request.GET.get('category_B')
    data_B = josaaTable.objects.filter(
        
        Category = category_value,
        Gender=gen_value,
        Institute = iit_value,
        Course = programtype_value,
        Programme = programname_value,
        Year=year_value
    ).values()
    data_B = list(data_B)
    return JsonResponse(data_B, safe=False)



# old .....

def get_graph_yearwise(request):
    
    gen_value = request.GET.get('gender')
    year_value = request.GET.get('year')
    iit_value = request.GET.get('institute')
    programtype_value = request.GET.get('course')
    programname_value = request.GET.get('programme')
    graph_data = josaaTable.objects.filter(
        
        Category = "OPEN",
        Gender=gen_value,
        Institute = iit_value,
        Course = programtype_value,
        Programme = programname_value
    ).values()

    graph_data = list(graph_data)

    return JsonResponse(graph_data, safe=False)