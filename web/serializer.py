from rest_framework import serializers
from .models import Contributors, Projects
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
        fields = ["role", "author_user_id","project_id"]


    def create_contributor(self, validated_data, **kwargs):
        print(self)
        author = Contributors.objects.create(
            role=validated_data["role"],
            author_user_id=validated_data["author_user_id"],
            project_id=validated_data["project_id"],
        )
        author.save()
        return author
