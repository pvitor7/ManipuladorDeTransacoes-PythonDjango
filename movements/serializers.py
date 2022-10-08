from rest_framework import serializers
from movements.models import Movement
from Store.serializers import StoreSerializer
from Transactions.serializers import TransactionSerializer


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ['file']
    
    def create(self, validated_data):

        for key, value in validated_data.items():
            for transaction in value:
               
                type_transaction = int(transaction[0:1])
                date = transaction[1:9]
                value = transaction[9:19]
                cpf = transaction[19:30]
                card = transaction[30:42]
                hour = transaction[42:48]
                owner_store = transaction[48:62]
                name_store = transaction[62:81]
                
                #está com erro porque retorna b' indicativo de bytes antes das strings
                
                properties_transaction = {type_transaction, date, value, cpf, card, hour, owner_store, name_store}
                
                print({type_transaction: type_transaction, date: date, hour: hour, value: value, cpf: cpf, card: card})
                import ipdb
                
                transaction_serializer = TransactionSerializer(data={'type_transaction': type_transaction, 'date': date, 'hour': hour, 'value': value, 'cpf': cpf, 'card': card})
                transaction_serializer.is_valid(raise_exception=True)
                transaction_serializer.save()
                
                ipdb.set_trace()
                
                store_serializer = StoreSerializer(data={name_store, owner_store})
                store_serializer.is_valid(raise_exception=True)
                store_serializer.save()
                

                print(properties_transaction)            
                # print(len(tipo), len(data), len(valor), len(cpf), len(cartao), len(hora), len(dono_da_loja), len(nome_da_loja))
                # print('***variáveis:',tipo, data, valor, cpf, cartao, hora, dono_da_loja, nome_da_loja)                
                
        return super().create(validated_data)