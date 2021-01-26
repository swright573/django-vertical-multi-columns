import pytest

@pytest.fixture()
def susan():
	return 'susan'
	
@pytest.fixture()
def peter():
	return 'peter'	
	

@pytest.mark.parametrize("credentials", [("susan"), ("peter")], indirect=["credentials"])
def test_login(credentials):
    return True
