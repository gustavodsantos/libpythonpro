from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'gustavodsantos',
        'id': 131466188,
        'avatar_url': 'https://avatars.githubusercontent.com/u/131466188?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('gustavodsantos')
    assert 'https://avatars.githubusercontent.com/u/131466188?v=4' == url
