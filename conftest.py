import pytest

from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinallizer(fixture.destroy)
    return fixture
