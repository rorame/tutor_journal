from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pupils, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PupilsSerializer


# custom pagination class
# class PupilAPIListPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

# adding 3 simple classes for better understanding how to work permissions
class PupilAPIList(generics.ListCreateAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # parser_classes = PupilAPIListPagination


class PupilAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilsSerializer
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsOwnerOrReadOnly, )


class PupilAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilsSerializer
    # permission_classes = (IsAdminUser, )
    # custom permission
    permission_classes = (IsAdminOrReadOnly, )

# viewset
# class PupilsViewSet(viewsets.ModelViewSet):
#     queryset = Pupils.objects.all()
#     serializer_class = PupilsSerializer
#
#     # @action(methods=['get'], detail=False)
#     # def category(self, request):
#     #     cats = Category.objects.all()
#     #     return Response({'cats': [c.name for c in cats]})
#
#     # def get_queryset(self):
#     #     pk = self.kwargs.get('pk')
#     #
#     #     if not pk:
#     #         return Pupils.object.all()[:3]
#     #
#     #     return Pupils.objects.filter(pk=pk)
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})



# class PupilsAPIList(generics.ListAPIView):
#     queryset = Pupils.objects.all()
#     serializer_class = PupilsSerializer
#
#
# class PupilsAPIUpdate(generics.UpdateAPIView):
#     queryset = Pupils.objects.all()
#     serializer_class = PupilsSerializer
#
#
# class PupilsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Pupils.objects.all()
#     serializer_class = PupilsSerializer


# Базовый класс APIView для представлений
# class PupilsAPIView(APIView):
#     def get(self, request):
#         # lst = Pupils.objects.all().values()
#         # return Response({'pupils': list(lst)})
#
#         # Введение в сериализацию. Класс Serializer
#         pup = Pupils.objects.all()
#         return Response({'pupils': PupilsSerializer(pup, many=True).data})
#
#     def post(self, request):
#         # Введение в сериализацию. Класс Serializer
#         serializers = PupilsSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)
#
#         # post_new = Pupils.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     cat_id=request.data['cat_id']
#         # )
#
#         # return Response({'puplis': PupilsSerializer(post_new).data})
#         # return Response({'pupils': model_to_dict(post_new)})
#
#         # когда сами прописываем create и save для serializers
#         serializers.save()
#         return Response({'pupils': serializers.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Pupils.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = PupilsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Pupils.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"delete": "delete post " + str(pk)})

# class PupilsAPIView(generics.ListAPIView):
#     queryset = Pupils.objects.all()
#     serializer_class = PupilsSerializer
