from rest_framework import serializers
from .models import Projects, Contributors, Issues
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

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ["title", "tag"]

    def create_issues(self, validated_data):
        issue = Issues.objects.create(
            title=validated_data["title"],
            tag=validated_data["tag"],
            project_id=self.project_id,
        )
        issue.save()
        return issue

