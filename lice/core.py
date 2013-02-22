from pkg_resources import (resource_stream, resource_listdir)
import argparse
import datetime
import re
import os
import subprocess
import sys
import getpass

__version__ = "0.2"

LICENSES = []
for file in sorted(resource_listdir(__name__, '.')):
    match = re.match(r'template-([a-z0-9_]+).txt', file)
    if match:
        LICENSES.append(match.groups()[0])

DEFAULT_LICENSE = "bsd3"


def clean_path(p):
    """ Clean a path by expanding user and environment variables and
        ensuring absolute path.
    """
    p = os.path.expanduser(p)
    p = os.path.expandvars(p)
    p = os.path.abspath(p)
    return p


def get_context(args):
    return {
        "year": args.year,
        "organization": args.organization,
        "project": args.project,
    }


def guess_organization():
    """ Guess the organization from `git config`. If that can't be found,
        fall back to $USER environment variable.
    """
    try:
        stdout = subprocess.check_output('git config --get user.name'.split())
        org = stdout.strip()
    except:
        org = getpass.getuser()
    return org.decode("UTF-8")


def load_file_template(path):
    """ Load template from the specified filesystem path.
    """
    if not os.path.exists(path):
        raise ValueError("path does not exist: %s" % path)
    with open(clean_path(path)) as infile:
        template = infile.read()
    return template


def load_package_template(license, header=False):
    """ Load license template distributed with package.
    """
    filename = 'template-%s-header.txt' if header else 'template-%s.txt'
    with resource_stream(__name__, filename % license) as licfile:
        content = licfile.read()
    return content


def extract_vars(template):
    """ Extract variables from template. Variables are enclosed in
        double curly braces.
    """
    keys = []
    for match in re.finditer(r"\{\{ (?P<key>\w+) \}\}", template):
        keys.append(match.groups()[0])
    return keys


def generate_license(template, context):
    """ Generate a license by extracting variables from the template and
        replacing them with the corresponding values in the given context.
    """
    for key in extract_vars(template):
        if key not in context:
            raise ValueError("%s is missing from the template context" % key)
        template = template.replace("{{ %s }}" % key, context[key])
    return template


def main():

    def valid_year(string):
        if not re.match(r"^\d{4}$", string):
            raise argparse.ArgumentTypeError("Must be a four digit year")
        return string

    parser = argparse.ArgumentParser(description='Generate a license')

    parser.add_argument('license', metavar='license', nargs="?", choices=LICENSES,
                       help='the license to generate, one of: %s' % ", ".join(LICENSES))
    parser.add_argument('--header', dest='header', action="store_true",
                       help='generate source file header for specified license')
    parser.add_argument('-o', '--org', dest='organization', default=guess_organization(),
                       help='organization, defaults to .gitconfig or os.environ["USER"]')
    parser.add_argument('-p', '--proj', dest='project', default=os.getcwd().split(os.sep)[-1],
                       help='name of project, defaults to name of current directory')
    parser.add_argument('-t', '--template', dest='template_path',
                       help='path to license template file')
    parser.add_argument('-y', '--year', dest='year', type=valid_year,
                       default="%i" % datetime.date.today().year,
                       help='copyright year')
    parser.add_argument('--vars', dest='list_vars', action="store_true",
                       help='list template variables for specified license')

    args = parser.parse_args()

    # do license stuff

    license = args.license or DEFAULT_LICENSE

    # generate header if requested

    if args.header:

        if args.template_path:
            template = load_file_template(args.template_path)
        else:
            try:
                template = load_package_template(license, header=True)
            except IOError:
                sys.stderr.write("Sorry, no source headers are available for %s.\n" % args.license)
                sys.exit(1)

        content = generate_license(template.decode("UTF-8"), get_context(args))
        sys.stdout.write(content)

        sys.exit(0)

    # list template vars if requested

    if args.list_vars:

        if args.template_path:
            template = load_file_template(args.template_path)
        else:
            template = load_package_template(license)

        var_list = extract_vars(template)

        if var_list:
            sys.stdout.write("The %s license template contains the following variables:\n" % (args.template_path or license))
            for v in var_list:
                sys.stdout.write("  %s\n" % v)
        else:
            sys.stdout.write("The %s license template contains no variables.\n" % (args.template_path or license))

        sys.exit(0)

    # create context

    if args.template_path:
        template = load_file_template(args.template_path)
    else:
        template = load_package_template(license)

    content = generate_license(template.decode("UTF-8"), get_context(args))
    sys.stdout.write(content)


if __name__ == "__main__":
    main()
