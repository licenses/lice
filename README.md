# lice: Generate license files for your projects

Generate a BSD-3 license:

    $ lice

Generate an MIT license:

    $ lice mit

Generate a BSD-3 license, specifying the year and organization to be used, writing to *LICENSE*:

    $ lice -y 2012 -o "Sunlight Foundation" > LICENSE
    
## Arguments

license
    One of: apache, bsd2, bsd3, cddl, eclipse, gpl2, gpl3, lgpl, mit, moz, public. Defaults to bsd3 if not specified.

-y, --year
    The copyright year.
    
-o, --org
    The organization. Pulls your name from `git config` or `$USER` if not specified.

-p, --proj
    The name of the project. Uses the current directory name if not specified.

-t, --template
    Path to a license template file. Overrides the license argument.
    