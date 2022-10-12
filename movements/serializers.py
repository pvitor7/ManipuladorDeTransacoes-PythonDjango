import ipdb
import locale
from rest_framework import serializers
from movements.models import Movement
from Store.models import Store
from Transactions.serializers import TransactionSerializer
import datetime


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ["file"]

    def create(self, validated_data):

        for transaction in validated_data["file"]:

            type_transaction = int(transaction[0:1])
            value = str(transaction[9:19], "utf-8")
            cpf = str(transaction[19:30], "utf-8")
            card = str(transaction[30:42], "utf-8")
            owner_store = str(transaction[48:62], "utf-8")
            name_store = str(transaction[62:81], "utf-8")

            date_transaction = str(transaction[1:9], "utf-8")
            date_convert = datetime.datetime.strptime(
                f"{int(date_transaction[6:8])}/{int(date_transaction[4:6])}/{int(date_transaction[0:4])}",
                "%d/%m/%Y",
            ).date()

            hour_transaction = str(transaction[42:48], "utf-8")
            hour = datetime.time(
                int(hour_transaction[0:2]),
                int(hour_transaction[2:4]),
                int(hour_transaction[4:6]),
            )

            locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
            currency_value = locale.currency(
                int(value[:-2]), grouping=True, symbol=None
            )

            operation = "Entrada"
            if type_transaction == 2 or type_transaction == 3 or type_transaction == 9:
                operation = "Saída"

            store = {"store": name_store, "owner": owner_store}
            ipdb.set_trace()
            store_pk, _ = Store.objects.get_or_create(**store)
            if _ == True:
                store_pk = Store.objects.get(store=name_store)


            transaction_serializer = TransactionSerializer(
                data={
                    "type_transaction": type_transaction,
                    "date": date_convert,
                    "hour": hour,
                    "value": currency_value,
                    "cpf": cpf,
                    "card": card,
                    "operation": operation,
                    "store": store_pk.id,
                }
            )
            transaction_serializer.is_valid(raise_exception=True)
            transaction_serializer.save()

        return "Informações armazenadas com sucesso!"
