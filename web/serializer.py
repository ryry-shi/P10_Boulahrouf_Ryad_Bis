from rest_framework import serializers
from .models import Projects, Contributors
from user.serializer import MyUserSerializer

class ProjectSerializer(serializers.ModelSerializer):


    class Meta:

        model = Projects
        fields = ["title", "description", "type"]

    def create_projects(self, validated_data):
        project = Projects.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author_user_id=self.id,
        )
        project.save()
        return project


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contributors
        fields = ["role"]


    def create_contributor(self, validated_data):
        author = Contributors.objects.create(
            role=validated_data["role"]
        )
        author.save()
        return author
    # def get_author_user_id(self, instance):
    #     queryset = instance.author_user_id
    #     serializer = MyUserSerializer(queryset)
    #     return serializer.data
    #      def get_products(self, instance):
    #     queryset = instance.products.filter(active=True)
    #     serializer = ProductListSerializers(queryset, many=True)
    #     return serializer.data