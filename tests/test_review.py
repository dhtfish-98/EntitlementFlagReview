import plistlib
import unittest
from review import review_bytes, review_text


class EntitlementTests(unittest.TestCase):
    def test_xml_and_binary(self):
        value = {"com.apple.security.get-task-allow": True, "com.apple.security.cs.allow-jit": False}
        for fmt in (plistlib.FMT_XML, plistlib.FMT_BINARY):
            with self.subTest(fmt=fmt):
                self.assertEqual([x["location"] for x in review_bytes(plistlib.dumps(value, fmt=fmt))], ["com.apple.security.get-task-allow"])

    def test_false_is_quiet(self):
        self.assertEqual(review_bytes(plistlib.dumps({"com.apple.security.get-task-allow": False})), [])

    def test_invalid(self):
        with self.assertRaises(ValueError):
            review_text("not plist")
