from rest_framework import serializers
from documentos.models import  docAnalisisModel, docPruebasUnitariasModel, docRequisitosModel, docRgistroRastreoModel, docPruebasModel 

class doc_analisis_Serializer1(serializers.ModelSerializer):
    class Meta:
        model = docAnalisisModel
        fields = ('__all__')

class doc_pruebasU_Serializer(serializers.ModelSerializer):
    class Meta:
        model = docPruebasUnitariasModel
        fields = ('__all__')

class doc_requisitos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = docRequisitosModel
        fields = ('__all__')

class doc_registroR_Serializer(serializers.ModelSerializer):
    class Meta:
        model = docRgistroRastreoModel
        fields = ('__all__')

class doc_Preubas_Serializer(serializers.ModelSerializer):
    class Meta:
        model = docPruebasModel
        fields = ('__all__')