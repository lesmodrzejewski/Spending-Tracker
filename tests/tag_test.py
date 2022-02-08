import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        self.tag = Tag("grocery", 7)

    def test_tag_has_name(self):
        self.assertEqual("grocery", self.tag.name)

    def test_tag_has_id(self):
        self.assertEqual(7, self.tag.id)