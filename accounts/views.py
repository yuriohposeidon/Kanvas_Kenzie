from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class RetrieveUpdateDeleteAccountView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
