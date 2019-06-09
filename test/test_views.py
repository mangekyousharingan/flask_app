import unittest
from mockupdb import MockupDB
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.server = MockupDB(auto_ismaster=True, verbose=True)
        self.server.run()
        app.config['TESTING'] = True
        app.config['MONGO_URI'] = self.server.uri
        self.app = app.test_client()

    @classmethod
    def tearDownClass(self):
        self.server.stop()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data.decode("utf-8")

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEquals({'imie': 'Natalia', 'mgs': 'Hello World!'}, rv.json)
