import unittest

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='victor', email='victor@mail.com', password='parseword')
        self.new_post = Post()
        self.new_comment = Comment()

    def test_user_instance(self):
        pass

    def test_post_instance(self):
        pass

    def test_comment_instance(self):
        pass


if __name__ == '__main__':
    unittest.main()
