from rest_framework import serializers

from customer.models import *

class GetcustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customer
        fields ="__all__"

class CustomeradressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer_Address
        fields = "__all__"


class CustomerDetailsAddressSerializer(serializers.ModelSerializer):
    customer_address = CustomeradressSerializer(many = True)

    class Meta:
        model = customer
        fields = ('first_name','last_name','mobile','age','country','city','dob')        