from lice.core import *
from io import StringIO
import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest


def collector():
    start_dir = os.path.abspath(os.path.dirname(__file__))
    return unittest.defaultTestLoader.discover(start_dir)


class TestPaths(unittest.TestCase):

    def test_paths(self):
        self.assertEqual(clean_path("."), os.getcwd())
        self.assertEqual(clean_path("$HOME"), os.environ["HOME"])
        self.assertEqual(clean_path("~"), os.environ["HOME"])

class TestTemplates(unittest.TestCase):

    def test_file_template(self):
        pwd = os.path.abspath(os.path.dirname(__file__))
        for license in LICENSES:
            path = os.path.join("license-templates", "templates", "%s.txt" % license)
            with open(path) as infile:
                content = infile.read()
                self.assertEqual(content, load_file_template(path).getvalue())

    def test_package_template(self):
        pwd = os.path.abspath(os.path.dirname(__file__))
        for license in LICENSES:
            path = os.path.join("license-templates", "templates", "%s.txt" % license)
            with open(path) as infile:
                self.assertEqual(infile.read(), load_package_template(license).getvalue())

    def test_extract_vars(self):
        template = StringIO()
        for license in LICENSES:
            template.write(u'Oh hey, {{ this }} is a {{ template }} test.')
            var_list = extract_vars(template)
            self.assertEquals(var_list, ["template", "this"])

    def test_license(self):

        context = {
            "year": u'1981',
            "project": u'lice',
            "organization": u'Awesome Co.'
        }

        for license in LICENSES:

            template = load_package_template(license)
            content = template.getvalue()

            content = content.replace(u'{{ year }}', context["year"])
            content = content.replace(u'{{ project }}', context["project"])
            content = content.replace(u'{{ organization }}', context["organization"])

            self.assertEqual(content, generate_license(template, context).getvalue())
            template.close() # discard memory

    def test_license_header(self):

        context = {
            "year": u'1981',
            "project": u'lice',
            "organization": u'Awesome Co.'
        }

        for license in LICENSES:

            try:

                template = load_package_template(license, header=True)
                content = template.getvalue()

                content = content.replace(u'{{ year }}', context["year"])
                content = content.replace(u'{{ project }}', context["project"])
                content = content.replace(u'{{ organization }}', context["organization"])

                self.assertEqual(content, generate_license(template, context).getvalue())
                template.close() # discard memory

            except IOError:
                pass  # it's okay to not find templates


if __name__ == '__main__':
    unittest.main()
