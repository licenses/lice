from core import *
import os
import unittest


class TestPaths(unittest.TestCase):
    
    def test_paths(self):
        self.assertEqual(clean_path("."), os.getcwd())
        self.assertEqual(clean_path("$HOME"), os.environ["HOME"])
        self.assertEqual(clean_path("~"), os.environ["HOME"])


class TestTemplates(unittest.TestCase):
    
    def test_file_template(self):
        pwd = os.path.abspath(os.path.dirname(__file__))
        for license in LICENSES:
            path = os.path.join(pwd, "template-%s.txt" % license)
            with open(path) as infile:
                self.assertEqual(infile.read(), load_file_template(path))
                
    def test_package_template(self):
        pwd = os.path.abspath(os.path.dirname(__file__))
        for license in LICENSES:
            path = os.path.join(pwd, "template-%s.txt" % license)
            with open(path) as infile:
                self.assertEqual(infile.read(), load_package_template(license))
    
    def test_extract_vars(self):
        for license in LICENSES:
            template = """Oh hey, {{ this }} is a {{ template }} test."""
            var_list = extract_vars(template)
            self.assertEquals(var_list, ["this", "template"])

    def test_license(self):
        
        context = {
            "year": "1981",
            "project": "lice",
            "organization": "Awesome Co.",
        }
        
        for license in LICENSES:
            
            template = load_package_template(license)
            
            rendered = template.replace("{{ year }}", context["year"])
            rendered = rendered.replace("{{ project }}", context["project"])
            rendered = rendered.replace("{{ organization }}", context["organization"])
            
            self.assertEqual(rendered, generate_license(template, context))


if __name__ == '__main__':
    unittest.main()
    