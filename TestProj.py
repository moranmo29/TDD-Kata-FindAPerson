import unittest

class Crowdmap(object):
    def get_all_posts_for(self,param):
        pass

class FindProj(unittest.TestCase):
    def setUp(self):
        self.Crowdmap=Crowdmap()
    def test_getAllPostsForName(self):
        posts= self.Crowdmap.get_All_Posts_for("Or")
        self.assertIn("Or", posts)


