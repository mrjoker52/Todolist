from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

#Get Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# การ Post data (save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

 
@api_view(['PUT'])
def upate_todolist(request,TID):
    # localhost:8000/api/update-todolist/(id เป็นตัวเลข)
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete: 
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode) 





data = [
    {
        "title" : "มาเขียนโปรแกรมกัน!",
        "subtitle" : "บทความนี้จะแนะนำการเริ่มต้นเขียนโปรแกรม",
        "image_url" : "https://raw.githubusercontent.com/mrjoker52/BaicAPI/main/computer_laptop.jpg",
        "detail" : "หมายถึง การเขียนหรือสร้างคำสั่งให้คอมพิวเตอร์ทำงานให้ได้ตามที่ต้องการ ด้วยภาษาที่คอมพิวเตอร์เข้าใจ (สามารถแปลได้) ในการเขียนโปรแกรมนี้ ผู้เขียนจะต้องเข้าใจถึงขั้นตอนการแก้ปัญหา วิธีการแก้ รวมทั้ง ศัพท์และไวยากรณ์ ตลอดจนกฎเกณฑ์ของภาษาที่เลือกใช้ ดู programming language ประกอบ"
    },
    {
        "title" : "Flutter คือ?",
        "subtitle" : "Tools สำหรับออกแบบ UI ของ Google",
        "image_url" : "https://raw.githubusercontent.com/mrjoker52/BaicAPI/main/flutter.jpg",
        "detail" : "ross-Platform Framework ที่ใช้ในการพัฒนา Native Mobile Application (Android/iOS) พัฒนาโดยบริษัท Google Inc. โดยใช้ภาษา Dart ในการพัฒนา ที่มีความคล้ายกับภาษา C# และ Java."
    },
    {
        "title" : "Python คือ?",
        "subtitle" : "ภาษาเขียนโปรแกรมชนิดหนึ่ง เขียนได้ง่ายมากๆ",
        "image_url" : "https://raw.githubusercontent.com/mrjoker52/BaicAPI/main/phone_App.jpg",
        "detail" : "ภาษาไพธอน (python) เป็นการเขียนโปรแกรมที่ได้นำข้อดีของภาษาต่างๆมารวไว้ด้วยกัน มีโค้ดคำสั่งเข้าใจง่ายและเขียนได้สั้นกว่าภาษาอื่นๆ ทำให้สามารถนำไปพัฒนาโปรแกรมที่มีขนาดใหญ่และมีความซับซ้อนได้อย่างสะดวก ด้วยเหตุนี้ไพธอนจึงได้รับความนิยม ใช้ในการเขียนโปรแกรม"
    }
]

def Home(request):
    return JsonResponse(data=data, safe=False,json_dumps_params={'ensure_ascii': False})
