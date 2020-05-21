from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import mixins, generics


class TransactionApiView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        qs = Transaction.objects.all()
        query = self.request.GET.get('user')
        if query is not None:
            qs = qs.filter(user=query)
        return qs


class TransactionDetailAPi(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
