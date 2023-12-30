
# Writng Djngo Views using serializers
#request.POST -- handles form data, it only works for 'POST'method
# request.data --handles arbitrary data, works for 'POST', 'PUT' and 'PATCH'
# rturn Response(data) -- response to content as requested by 
# restframework provides two wrappers you can use to write API views
# eg @api_view and APIView

# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializer import SnippetSerializer
# from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

# writing Api using class based views
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404 

# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status =status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    

# """Retrieve, update or delete a snippet instance."""""    
# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         """return specific object based on primary key"""
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         """
#         retrieve detail for a specific result using the GET request
        
#         """
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
    
#     def put(self, request, pk, format=None):
#         """CRUD operation in restful API using PUT method"""
#         # retrieve existing snippet object with the specified primary key
#         snippet = self.get_object(pk)
#         # create serializer instance with retrieved snippet object
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # return a response with serialized data of the updated snippet
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# using mixins


from snippets.models import Snippet
from snippets.serializer import SnippetSerializer
# from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

# class SnippetList(mixins.ListModelMixin, # .list() function
#                   mixins.CreateModelMixin, # .create() function
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class SnippetDetail(mixins.RetrieveModelMixin, # .retrieve() function
#                     mixins.UpdateModelMixin,  # .update() function
#                     mixins.DestroyModelMixin, # .destroy() function
#                     generics.GenericAPIView):  
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

"""Using generic class based views"""
class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
          
    def perfom_create(self, serializer):
        serializer.save(owner=self.request.user)



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
# from django.contrib.auth.models import User
# from .serializer import UserSerializer


# """Read-only views for user representation"""
# class UserList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = User.objects.all() # retrieve data from list view
#     serializer_class = UserSerializer
    
#     def perfom_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all() # retrieve data from detail view
#     serializer_class = UserSerializer
    