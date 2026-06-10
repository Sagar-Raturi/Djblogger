import factory
from django.contrib.auth.models import User
from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    #    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password123")
    is_staff = True
    is_superuser = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = "published"
