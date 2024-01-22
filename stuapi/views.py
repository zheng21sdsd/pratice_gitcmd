from django.shortcuts import render
from django.views import View
import json
from stuapi.models import Student
from django.http.response import JsonResponse
# Create your views here.
### 这个是用Django原生 来实现接口api的
# 我知道我们都有问题，大家都好好好的配合才可以完成我们的工作

'''
POST /students/ 添加一个学生信息
GET /students/  获取所有学生信息

GET/students/<pk>/  获取一个学生信息
PUT /students/<pk>/  修改一个学生信息
DELETE /students/<pk>  删除一个学生信息
一个路由对应一个视图类  随意我们可以把五个API分成两个类来完成任务
'''
class StudentView(View):
    def post(self,request):
        '''添加一个学生信息'''
        # 1.接收客户端提交的数据验证客户端的数据
        data = json.loads(request.body.decode())
        name = data.get('name')
        sex = data.get('sex')
        age = data.get('age')
        classmate = data.get('classmate')
        description = data.get('description')
        # 2.操作数据库  保存数据
        # Student.object.filter(name=name).exists()
        instance = Student.objects.create(
            name = name,
            sex = sex,
            age = age,
            classmate = classmate,
            description = description,
        )
        ##  返回结果
        return JsonResponse(
            data = {
                'id':instance.pk,
                'name':instance.name,
                'sex':instance.sex,
                'age':instance.age,
                'classmate':instance.description,
                'description':instance.description,

            },status = 201
        )
    def get(self,request):
        '''获取多个学生信息'''
        # 1.读取数据库
        students_list = list(Student.objects.values())
        ## 返回数据
        return JsonResponse(
            data = students_list,status =200,safe = False
        )
class StudentInfoView(View):
    def get(self,request,pk):
        '''获取一条数据'''
        try:
            instance = Student.objects.get(pk = pk)### instance 就是一个实例对象
            return JsonResponse(data = {
                'id':instance.pk,
                'name':instance.name,
                'sex':instance.sex,
                'age':instance.age,
                'classmate':instance.classmate,
                'description':instance.description,
            },status = 200)
        except Student.DoesNotExist:
            return JsonResponse(data = None,status =404)
        ### 没有内容的时候返回404
    def put(self,request,pk):
        '''更新一个学生信息'''
        # 1.接受客户但提交的数据 ，验证客户端的数据
        # data = json.loads(request.body.decode())
        data = json.loads(request.body)
        name = data.get('name')  # alt+j 选中多个一样的
        sex = data.get('sex')
        age = data.get('age')
        classmate = data.get('classmate')
        description = data.get('description')

        # 2.操作数据库  保存数据
        try:
            instance = Student.object.get(pk = pk)
            instance.name = name
            instance.age = age
            instance.sex = sex
            instance.age = age
            instance.classmate = classmate
            instance.description = description
            instance.save()
        except Student.DoseNoeExist:
            return JsonResponse(data = {},status = 404)
        ##返回结果
        return JsonResponse(data = {
            "id": instance.pk,
            "name": instance.name,
            "sex": instance.sex,
            "age": instance.age,
            "classmate": instance.classmate,
            "description": instance.description,
        },status=201)

    def delete(self, request, pk):
        """删除一个学生信息"""
        try:
            Student.objects.filter(pk=pk).delete()
        except:
            pass
        return JsonResponse(data={}, status=204)
