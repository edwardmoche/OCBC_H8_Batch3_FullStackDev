import unittest
from app import connex_app 


class TestAPI(unittest.TestCase):

    def test_getdirectors(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/directors")
        self.assertEqual(response.status_code, 200, "should be displaying list of directors")

    def test_getmovies(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/movies")
        self.assertEqual(response.status_code, 200, "should be displaying list of movies")

          


if __name__ == '__main__':
    unittest.main()