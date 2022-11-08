from rest_framework import serializers


class SelfFollowingValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        values = [value[field_name] for field_name in self.fields]
        if len(values) != len(set(values)):
            # текст сообщения об ошибке имеет надо будет изменить,
            # когда станут понятны варианты использования валидатора
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя (или что вы там затеяли)!')
