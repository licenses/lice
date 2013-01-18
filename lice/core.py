from pkg_resources import resource_stream
import argparse
import datetime
import re
import os
import subprocess
import sys

__version__ = "0.1"

LICENSES = ["apache", "bsd2", "bsd3", "cddl", "eclipse",
            "gpl2", "gpl3", "lgpl", "mit", "moz", "public"]
DEFAULT_LICENSE = "bsd3"


def guess_organization():
    
    try:        
        stdout = subprocess.check_output('git config --get user.name'.split())
        org = stdout.strip()
    except OSError:
        org = os.environ["USER"]
        
    return org


def load_template(license):
    with resource_stream(__name__, 'template-%s.txt' % license) as licfile:
        content = licfile.read()
    return content


def extract_vars(template):
    keys = []
    for match in re.finditer(r"\{\{ (?P<key>\w+) \}\}", template):
        keys.append(match.groups()[0])
    return keys


def generate_license(license, context):
    
    template = load_template(license)
    
    for key in extract_vars(template):
        
        if key not in context:
            raise ValueError("%s is missing from the template context" % key)
        
        template = template.replace("{{ %s }}" % key, context[key])
    
    return template

def main():
    
    parser = argparse.ArgumentParser(description='Generate a license')
    parser.add_argument('license', metavar='license', nargs="?",
                       help='the license to generate, one of: %s' % ", ".join(LICENSES))
    parser.add_argument('-o', '--org', dest='organization',
                       help='organization, defaults to .gitconfig or os.environ["USER"]')
    parser.add_argument('-p', '--proj', dest='project',
                       help='name of project, defaults to name of current directory')
    parser.add_argument('-t', '--template', dest='template',
                       help='path to license template file')
    parser.add_argument('-y', '--year', dest='year',
                       help='copyright year')

    args = parser.parse_args()

    # check year, if specified
        
    if args.year and not re.match(r"^\d{4}$", args.year):
        parser.error("-y must be a four digit year")

    # create context
    
    context = {
        "year": args.year or "%i" % datetime.date.today().year,
        "organization": args.organization or guess_organization(),
        "project": args.project or os.getcwd().split(os.sep)[-1],
    }

    if args.template:
        pass
        
    else:

        license = args.license or DEFAULT_LICENSE

        if license not in LICENSES:
            parser.error("license must be one of: %s" % ", ".join(LICENSES))
            
        content = generate_license(license, context)
        sys.stdout.write(content)


if __name__ == "__main__":
    main()