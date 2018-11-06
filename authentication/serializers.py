# Django
from django.contrib.auth import authenticate
from rest_framework import serializers

# Local Django
from profile.serializers import ProfileSerializer
from authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)
    first_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    city = serializers.CharField(max_length=50, required=False)
    state = serializers.CharField(max_length=50, required=False)
    country = serializers.CharField(max_length=50, required=False)
    is_superuser = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = [
            'email', 'username', 'password',
            'token', 'first_name', 'last_name',
            'city', 'state', 'country', 'is_superuser'
        ]

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        if validated_data['is_superuser']:
            return User.objects.create_superuser(validated_data)
        return User.objects.create_user(validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=False)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        password = data.get('password', None)
        username = data.get('username', None)

        # Raise an exception if an
        # username is not provided.
        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `username` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `username`.
        user = authenticate(username=username, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag is to tell us whether the user has been banned
        # or deactivated. This will almost never be the case, but
        # it is worth checking. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserUpdateSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    # Passwords must be at least 8 characters, but no more than 128
    # characters. These values are the default provided by Django. We could
    # change them, but that would create extra work while introducing no real
    # benefit, so lets just stick with the defaults.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        required=False
    )

    # When a field should be handled as a serializer, we must explicitly say
    # so. Moreover, `UserSerializer` should never expose profile information,
    # so we set `write_only=True`.
    profile = ProfileSerializer(write_only=True, required=False)

    # We want to get the `bio` and `image` fields from the related Profile
    # model.
    bio = serializers.CharField(source='profile.bio', required=False, allow_null=True, allow_blank=True)
    image = serializers.CharField(source='profile.image', required=False, allow_null=True, allow_blank=True)
    cover = serializers.CharField(source='profile.cover', required=False, allow_null=True, allow_blank=True)
    first_name = serializers.CharField(max_length=20, required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=20, required=False, allow_null=True, allow_blank=True)
    city = serializers.CharField(max_length=50, required=False, allow_null=True, allow_blank=True)
    state = serializers.CharField(max_length=50, required=False, allow_null=True, allow_blank=True)
    country = serializers.CharField(max_length=50, required=False, allow_null=True, allow_blank=True)

    is_superuser = serializers.NullBooleanField(write_only=True)
    is_staff = serializers.NullBooleanField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password',
            'token', 'first_name', 'last_name',
            'profile', 'bio', 'image', 'city', 'state', 'country',
            'is_staff', 'is_superuser', 'cover'
        )

        # The `read_only_fields` option is an alternative for explicitly
        # specifying the field with `read_only=True` like we did for password
        # above. The reason we want to use `read_only_fields` here is that
        # we don't need to specify anything else about the field. The
        # password field needed the `min_length` and
        # `max_length` properties, but that isn't the case for the token
        # field.
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        # Passwords should not be handled with `setattr`, unlike other fields.
        # Django provides a function that handles hashing and
        # salting passwords. That means
        # we need to remove the password field from the
        # `validated_data` dictionary before iterating over it.
        password = validated_data.pop('password', None)

        # Like passwords, we have to handle profiles separately. To do that,
        # we remove the profile data from the `validated_data` dictionary.
        profile_data = validated_data.pop('profile', {})

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            setattr(instance, key, value)

        if password is not None:
            # `.set_password()`  handles all
            # of the security stuff that we shouldn't be concerned with.
            instance.set_password(password)

        # After everything has been updated we must explicitly save
        # the model. It's worth pointing out that `.set_password()` does not
        # save the model.
        instance.save()

        for (key, value) in profile_data.items():
            # We're doing the same thing as above, but this time we're making
            # changes to the Profile model.
            setattr(instance.profile, key, value)

        # Save the profile just like we saved the user.
        instance.save()

        return instance
