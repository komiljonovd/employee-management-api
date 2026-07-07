from employeeapp.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Employee
        fields = ['id',
                  'department',
                  'department_name',
                  'first_name',
                  'last_name',
                  'email',
                  'created_at'
                  ]
        
        read_only_fields = ['id','created_at']

    def to_representation(self, instance):

        fields =  super().to_representation(instance)
        request = self.context.get('request')
        if request and request.method == 'GET':
            fields.pop('created_at')

        return fields
    


    def validate_email(self, value):

        value = value.lower().strip()
        if '@' in value:
            index = value.index('@')
            if len(value[:index]) < 6:
                raise serializers.ValidationError("Incorrect format of Email")
    
        return value
    
    def validate(self, attrs: dict) -> dict:

        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')

        print(attrs)

        if first_name == last_name:
            raise serializers.ValidationError(
                {"last_name": "The last name cannot be the same as the first name."}
            )
        
        if len(first_name.strip()) < 2:
            raise serializers.ValidationError({'first_name':'at least 4 letters'})
        
        if not first_name.isalpha():
            raise serializers.ValidationError({'first_name':' must consist only of letters.'})
        
        if len(last_name.strip()) < 2:
            raise serializers.ValidationError({'last_name':'at least 4 letters'})
        
        if not last_name.isalpha():
            raise serializers.ValidationError({'last_name':' must consist only of letters.'})
         
        return attrs
