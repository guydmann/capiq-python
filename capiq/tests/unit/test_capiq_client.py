import unittest

from mock import mock

from capiq.capiq_client import CapIQClient

orig_import = __import__

class TestCapiqClient(unittest.TestCase):

    def test_verify_true(self):
        ciq_client = CapIQClient("username", "password", verify=True)
        self.assertEqual(ciq_client.verify, True)

    def test_verify_false(self):
        ciq_client = CapIQClient("username", "password", verify=False)
        self.assertEqual(ciq_client.verify, False)

    def test_python_2_exception(self):
        def import_mock(name, *args):

            if name == 'http.client':
                raise ImportError
            return orig_import(name, *args)

        with mock.patch('builtins.__import__', side_effect=import_mock):
            capiq_client = CapIQClient("username", "password", verify=False)
            self.assertIsInstance(capiq_client, CapIQClient)