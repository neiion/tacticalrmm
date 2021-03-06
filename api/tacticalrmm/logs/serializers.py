from rest_framework import serializers

from .models import PendingAction


class PendingActionSerializer(serializers.ModelSerializer):

    hostname = serializers.ReadOnlyField(source="agent.hostname")
    salt_id = serializers.ReadOnlyField(source="agent.salt_id")
    client = serializers.ReadOnlyField(source="agent.client")
    site = serializers.ReadOnlyField(source="agent.site")
    due = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()

    class Meta:
        model = PendingAction
        fields = "__all__"
