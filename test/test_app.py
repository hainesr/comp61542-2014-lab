from os import path
import unittest
import comp61542

class TestApp(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        data = "dblp_curated_sample.xml"
        comp61542.app.config['TESTING'] = True
        comp61542.app.config['DATASET'] = data
        comp61542.app.config['DATABASE'] = path.join(dir, "..", "data", data)
        self.app = comp61542.app.test_client()

    def test_home(self):
        r = self.app.get("/")
        self.assertEqual(200, r.status_code, "Status code was not 'OK'.")

if __name__ == '__main__':
    unittest.main()
