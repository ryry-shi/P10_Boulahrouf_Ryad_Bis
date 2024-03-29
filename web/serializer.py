from rest_framework import serializers
from .models import Contributors, Issue, Projects, Comment
from user.serializer import MyUserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["title", "description", "type", "project_id", "author_user_id", "pk"]
        read_only_fields = ["project_id", "author_user_id", "pk"]

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
        fields = ["role", "user_id", "project_id", "id"]
        read_only_fields = ["project_id", "id"]

    def create_author(self, validated_data):
        author = Contributors.objects.create(
            role=validated_data["role"],
            user_id=validated_data["user_id"],
        )
        author.save()
        return author


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "title",
            "tag",
            "desc",
            "author_user_id",
            "assignee_user_id",
            "project_id",
            "id",
            "priority",
            "status",
        ]
        read_only_fields = ["project_id", "id", "author_user_id", "assignee_user_id"]

    def create_issue(self, validated_data):
        issue = Issue.objects.create(
            title=validated_data["title"],
            tag=validated_data["tag"],
            desc=validated_data["desc"],
            project_id=validated_data["project_id"],
            author_user_id=validated_data["author_user_id"],
            assignee_user_id=validated_data["assignee_user_id"],
            priority=validated_data["priority"],
            status=validated_data["status"],
        )
        issue.save()
        return issue


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["description", "author_user_id", "created_time", "id", "issue"]
        read_only_fields = ["author_user_id", "created_time", "issue"]

        def create_comment(self, validated_data):
            comment = Comment.objects.create(
                description=validated_data["description"],
                author_user_id=validated_data["author_user_id"],
                created_time=validated_data["created_time"],
                issue=validated_data["issue"]
            )
            comment.save()
            return comment
