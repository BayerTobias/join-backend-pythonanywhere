from rest_framework import serializers
from join.models import Task, Category, CustomUser, Contact


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    """

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["author", "assigned_users"]


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.
    """

    class Meta:
        model = Category
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for list view of CustomUser model.
    """

    class Meta:
        model = CustomUser
        fields = ["id", "initials", "color", "first_name", "last_name"]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for detail view of CustomUser model.
    """

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "initials",
            "color",
            "first_name",
            "last_name",
            "email",
        ]


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for Contact model.
    """

    class Meta:
        model = Contact
        fields = ["id", "name", "email", "phone", "initials", "color"]
