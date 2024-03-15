#!/usr/bin/env python3
"""
Unittests for check_urls.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
import json
import sys
from scripts import check_urls

class TestCheckUrls(unittest.TestCase):
    """
    TestCheckUrls class with unittest for check_urls.py
    """

    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    @patch('builtins.open', unittest.mock.mock_open(read_data='{"urls": []}'))
    def test_check_urls_empty(self):
        """
        Test that check_urls handles an empty URLs list without error.
        """
        check_urls.check_urls(json.loads('{"urls": []}'))
        self.assertIn('No URLs to check.', sys.stdout.getvalue())

    @patch('builtins.open', unittest.mock.mock_open(
        read_data='{"urls": [{"name": "Test", "url": "http://example.com"}]}'))
    @patch('requests.get')
    def test_check_url_success(self, mock_get):
        """
        Test check_urls successfully finds a specified string in the response.
        """
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = 'Success'
        mock_get.return_value = mock_response

        check_urls.check_urls(json.loads(
            '{"urls": [{"name": "Test", "url": "http://example.com", "contains": "Success"}]}'))
        self.assertIn('✅', sys.stdout.getvalue())

    @patch('builtins.open', unittest.mock.mock_open(
        read_data='{"urls": [{"name": "Test", "url": "http://example.com"}]}'))
    @patch('requests.get')
    def test_check_url_fail(self, mock_get):
        """
        Test check_urls correctly handles a failed URL check.
        """
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        check_urls.check_urls(json.loads
            ('{"urls": [{"name": "Test", "url": "http://example.com"}]}'))
        self.assertIn('❌', sys.stdout.getvalue())

    @patch('sys.exit')
    def test_read_json_file_not_found(self, mock_exit):
        """
        Test read_json_file properly handles a file not found scenario.
        """
        with patch('builtins.open', side_effect=FileNotFoundError):
            check_urls.read_json_file('nonexistent_file.json')
            mock_exit.assert_called_with(1)

    @patch('sys.exit')
    def test_read_json_file_invalid_json(self, mock_exit):
        """
        Test read_json_file properly handles an invalid JSON file.
        """
        with patch('builtins.open', unittest.mock.mock_open(read_data='{invalid_json: ')):
            check_urls.read_json_file('invalid.json')
            mock_exit.assert_called_with(1)

if __name__ == '__main__':
    unittest.main()
