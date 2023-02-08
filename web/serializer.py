from rest_framework import serializers
from .models import Projects
from user.serializer import MyUserSerializer

class ProjectSerializer(serializers.ModelSerializer):


    class Meta:

        model = Projects
        fields = ["title", "description", "type", "author_user_id"]

    def create_projects(self, validated_data):
        project = Projects.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
        )
        # project.author_user_id = MyUser.objects.get(pk='id')
        project.save()
        return project

    # def get_author_user_id(self, instance):
    #     queryset = instance.author_user_id
    #     serializer = MyUserSerializer(queryset)
    #     return serializer.data
    #      def get_products(self, instance):
    #     queryset = instance.products.filter(active=True)
    #     serializer = ProductListSerializers(queryset, many=True)
    #     return serializer.data