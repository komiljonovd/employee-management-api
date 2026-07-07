from employeeapp.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id','name','created_at']
        read_only_fields = ['id','created_at']

    def to_representation(self, instance):

        fields =  super().to_representation(instance)
        request = self.context.get('request')
        if request.method == 'GET':
            fields.pop('created_at')

        return fields
