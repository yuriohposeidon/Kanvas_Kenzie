from rest_framework.views import APIView, status, Request, Response
from .mixins import CreateModelsMixin, ListModelMixin, RetrieveModelMixin, DestroyModeMixin, UpdateModelMixin
from django.shortcuts import get_object_or_404


class GenericView(APIView):
    queryset = None
    serializer_class = None

class CreateAPIView(GenericView, CreateModelsMixin):
    def post(self, request: Request) -> Response:
        return super().create(request)
    
class ListAPIView(GenericView, ListModelMixin):
    def get(self, request: Request) -> Response:
        return super().list(request)
    
class ListCreateAPIView(ListAPIView, CreateAPIView):
    ...
    
    
class RetrieveAPIView(GenericView, RetrieveModelMixin):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrieve(request, pk)  
    
class UpdateAPIView(GenericView, UpdateModelMixin):
    def patch(self, request: Request, pk: int) -> Response:
        return super().partial_update(request, pk)
    
class DestroyAPIView(GenericView, DestroyModeMixin):
    def delete(self, request: Request, pk: int) -> Response:
        return super().destroy(request, pk)   
    

class RetrieveUpdateDestroyAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    ...