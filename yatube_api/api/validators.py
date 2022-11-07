from rest_framework import serializers


class SelfFollowingValidator:
    def __call__(self, value):
        if value['user'] == value['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
