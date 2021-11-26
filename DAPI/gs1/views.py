from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def Student_info(request):
#     if request.method == 'GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu=Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(serializer.errors)
#     if request.method=='POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data created'}
#             return JsonResponse(res,safe=False)
#         return JsonResponse(serializer.error)
#     if request.method=='PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         serializer = StudentSerializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data updated'}
#             return JsonResponse(res,safe=False)
#         return JsonResponse(serializer.error)
#     if request.method=='DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res={'msg':'data deleted '}
#         return JsonResponse(res,safe=False)
#         return JsonResponse(serializer.error)


from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data updated'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted '}
        return JsonResponse(res,safe=False)
        return JsonResponse(serializer.errors)


