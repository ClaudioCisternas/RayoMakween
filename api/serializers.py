from rest_framework import serializers
from rayoMakween.models import Trabajo

#creacion de modelos a serializar

class TrabajoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trabajo
        fields = ["nombre","diagnostico","fecha","materiales","publicar","comentario","usuario"]
