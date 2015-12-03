from rest_framework import serializers
from movies.models import Movies


class MoviesSerializer(serializers.Serializer):
    """
    Serializer class for model Movies.
    """
    pk = serializers.IntegerField(read_only=True)
    movie_title = serializers.CharField(required=True, allow_blank=False, max_length=50)
    user_rating = serializers.IntegerField(required=False)
    critics_rating = serializers.IntegerField(required=False)
    running_time_minutes = serializers.IntegerField(required=True)
    release_date = serializers.DateField(required=True)
    movie_description = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        """
        Create and return a new `Movies` instance, given the validated data.
        :param validated_data:
        :return:
        """
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movies` instance, given the validated data.
        :param instance:
        :param validated_data:
        :return:
        """
        instance.movie_title = validated_data.get('movie_title', instance.title)
        instance.user_rating = validated_data.get('user_rating', instance.user_rating)
        instance.critics_rating = validated_data.get('critics_rating', instance.critics_rating)
        instance.running_time_minutes = validated_data.get('running_time_minutes', instance.running_time_minutes)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.movie_description = validated_data.get('movie_description', instance.movie_description)
        instance.save()

        return instance
