from rest_framework import serializers
from .models import Contributors, Issue, Projects
from user.serializer import MyUserSerializer

class ProjectSerializer(serializers.ModelSerializer):


    class Meta:

        model = Projects
        fields = ["title", "description", "type"]
# 
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
        fields = ["role", "author_user_id", "project_id"]
        read_only_fields = ["project_id"]

    def create_author(self, validated_data, **kwargs):
        author = Contributors.objects.create(
            role=validated_data["role"],
            author_user_id= validated_data["author_user_id"],
        )
        author.save()
        return author



    

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Issue
        fields = ["title", "tag", "author_user_id", "assignee_user_id", "project_id"]
        read_only_fields = ["project_id"]

    def create_issue(self, validated_data, **kwargs):
        issue = Issue.objects.create(
            title=validated_data["title"],
            tag=validated_data["tag"],
            project_id=validated_data["project_id"],
            author_user_id= validated_data["author_user_id"],
            assignee_user_id= validated_data["assignee_user_id"]
        )
        issue.save()
        return issue
