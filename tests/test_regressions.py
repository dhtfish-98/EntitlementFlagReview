import json
import plistlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from review import review_bytes


class RegressionTests(unittest.TestCase):

    def test_wrong_type_xml_and_duplicate_key(self):
        with self.assertRaises(ValueError): review_bytes(plistlib.dumps({"com.apple.security.get-task-allow":"true"}))
        with self.assertRaises(ValueError): review_bytes(b'<?xml version="1.0"?><plist><dict>')
        with self.assertRaises(ValueError): review_bytes(b'<?xml version="1.0"?><plist version="1.0"><dict><key>com.apple.security.get-task-allow</key><true/><key>com.apple.security.get-task-allow</key><false/></dict></plist>')
