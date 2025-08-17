import os
import tempfile
import unittest

from file_searcher.search import search_by_extension, search_by_name


class TestFileSearcher(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.path = self.test_dir.name

        self.files = {
            "report1.txt": "Some content",
            "Report2.TXT": "Some more content",
            "notes.md": "Markdown content",
            "script.py": "print('hello')",
            "summary.docx": "Document content",
            "README": "No extension file",
        }

        for name, content in self.files.items():
            with open(os.path.join(self.path, name), "w") as f:
                f.write(content)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_search_by_extension_single(self):
        result = search_by_extension(self.path, ["txt"])
        expected = {
            os.path.join(self.path, "report1.txt"),
            os.path.join(self.path, "Report2.TXT"),
        }
        self.assertEqual(set(result), expected)

    def test_search_by_extension_multiple(self):
        result = search_by_extension(self.path, ["md", "py"])
        expected = {
            os.path.join(self.path, "notes.md"),
            os.path.join(self.path, "script.py"),
        }
        self.assertEqual(set(result), expected)

    def test_search_by_name_case_insensitive(self):
        result = search_by_name(self.path, "report")
        expected = {
            os.path.join(self.path, "report1.txt"),
            os.path.join(self.path, "Report2.TXT"),
        }
        self.assertEqual(set(result), expected)

    def test_search_by_name_no_matches(self):
        result = search_by_name(self.path, "nonexistentfile")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
