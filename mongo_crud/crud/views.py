from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from crud.models import Student
from crud.serializers import StudentSerializers


class CreateStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

#
# class Same(APIView):
#     def get(self,request):
#         a = Student.objects.values()
#         print(a)
#         return Response(a, status=200)


class DeleteData(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class DeleteAllData(APIView):
    def post(self, request):
        querry = Student.objects.all().delete()
        return Response("Deleted all")


class Search(APIView):
    def get(self, request, hh):
        print(Student.objects.filter(pk=hh))
        pk=hh
        querry = Student.objects.filter(Q(name__contains=pk) | Q(standard__contains=pk) | Q(roll__contains=pk) |
                                        Q(essay_topic__contains=pk) | Q(essay__contains=pk), id__contains=pk)
        print(querry)
        return Response(querry.values())
