import pytest
from unittest import mock

from requests import Response, HTTPError
from graphy.model import get


class MockResponse(Response):

    def __init__(self, url, status, reason, data):
        super()
        self.url = url
        self.status_code = status
        self.reason = reason
        self.data = data

    def json(self):
        return self.data


class TestDataAccess:

    @mock.patch('graphy.settings')
    @mock.patch('graphy.model.requests')
    def test_get(self, mock_request, mock_settings):
        mock_request.get.return_value = MockResponse('/url', 200, 'OK', {'foo': 'bar'})
        import pdb; pdb.set_trace()
        resp = get('/url')
        assert resp == {'foo': 'bar'}

    @mock.patch('graphy.settings')
    @mock.patch('graphy.model.requests')
    def test_get_raises_for_status(self, mock_request, mock_settings):
        mock_request.get.return_value = MockResponse('/url', 404, 'NOT FOUND', {})
        with pytest.raises(HTTPError):
            _ = get('/url')


