import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_method(self, post_factory):
        post = post_factory(title="test-post")
        assert post.__str__() == "test-post"
