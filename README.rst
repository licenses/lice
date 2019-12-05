====
lice
====


Lice generates license files. No more hunting down licenses from other projects.

Installation
------------

About what you'd expect::

    pip install lice


Overview
--------

Generate a BSD-3 license, the default::

    $ lice
    Copyright (c) 2013, Jeremy Carbaugh

    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    ...

Generate an MIT license::

    $ lice mit
    The MIT License (MIT)
    Copyright (c) 2013 Jeremy Carbaugh

    Permission is hereby granted, free of charge, to any person obtaining a copy
    ...

Generate a BSD-3 license, specifying the year and organization to be used::

    $ lice -y 2012 -o "Sunlight Foundation"
    Copyright (c) 2012, Sunlight Foundation

    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    ...

Generate a BSD-3 license, formatted for python source file::
 
    $ lice -l py

    # Copyright (c) 2012, Sunlight Foundation
    #
    # All rights reserved.
    #
    # Redistribution and use in source and binary forms, with or without modification,
    ...

Generate a python source file with a BSD-3 license commented in the header::
 
    $ lice -l py -f test
    $ ls
    test.py
    $ cat test.py

    # Copyright (c) 2012, Sunlight Foundation
    #
    # All rights reserved.
    #
    # Redistribution and use in source and binary forms, with or without modification,
    ...

Generate a source file (language detected by -f  extension)::

    $ lice -f test.c && cat test.c
    /*
     * Copyright (c) 2012, Sunlight Foundation
     *
     * All rights reserved.
     *
     * Redistribution and use in source and binary forms, with or without modification,
    ...


If organization is not specified, lice will first attempt to use `git config` to find your name. If not found, it will use the value of the $USER environment variable. If the project name is not specified, the name of the current directory is used. Year will default to the current year.

You can see what variables are available to you for any of the licenses::

    $ lice --vars mit
    The mit license template contains the following variables:
      year
      organization


I want XXXXXXXXX license in here!
---------------------------------

Great! Is it a license that is commonly used? If so, open an issue or, if you are feeling generous, fork and submit a pull request.


Usage
-----
::

    usage: lice [-h] [-o ORGANIZATION] [-p PROJECT] [-t TEMPLATE_PATH] [-y YEAR]
                [--vars] [license]

    positional arguments:
      license               the license to generate, one of: agpl3, apache, bsd2,
                            bsd3, cddl, cc0, epl, gpl2, gpl3, lgpl, mit, mpl

    optional arguments:
      -h, --help            show this help message and exit
      -o ORGANIZATION, --org ORGANIZATION
                            organization, defaults to .gitconfig or
                            os.environ["USER"]
      -p PROJECT, --proj PROJECT
                            name of project, defaults to name of current directory
      -t TEMPLATE_PATH, --template TEMPLATE_PATH
                            path to license template file
      -y YEAR, --year YEAR  copyright year
      -l LANGUAGE, --language LANGUAGE
                            format output for language source file, one of: js, f,
                            css, c, m, java, py, cc, h, html, lua, erl, rb, sh,
                            f90, hpp, cpp, pl, txt [default is not formatted (txt)]
      -f OFILE, --file OFILE Name of the output source file (with -l, extension can be omitted)
      --vars                list template variables for specified license


Changelog
---------

**0.6**

* Add PowerShell support (thanks to `danijeljw <https://github.com/danijeljw>`_)
* Add Rust support (thanks to `alex179ohm <https://github.com/alex179ohm>`_)
* Bugfixes (thanks to `ganziqim <https://github.com/ganziqim>`_)
* Added support for Python 3.7 and 3.8, removed support for Python 3.4

Tested against Python 2.7, 3.5, 3.6, 3.7, and 3.8.

**0.5**

* Add support for SCM alias for lisp-style comments (thanks to `ejmr <https://github.com/ejmr>`_)
* Additional support for WTFPL and GPL2 licenses (thanks to `ejmr <https://github.com/ejmr>`_)
* Support for Python 3.4 and 3.5 (thanks to `ejmr <https://github.com/ejmr>`_)

**0.4**

* Use ASCII instead of Unicode for templates (thanks to `tabletcorry <https://github.com/tabletcorry>`_)
* Add Academic Free License ("AFL") v. 3.0 (thanks to `brianray <https://github.com/brianray>`_)
* Add ISC (thanks to `masklinn <https://github.com/masklinn>`_)
* Add tox support for testing (thanks to `lukaszb <https://github.com/lukaszb>`_)
* Show defaults when listing template variables

**0.3**

* Generate source file headers for some liceneses
* Discover available licenses at runtime
* Use getpass module for retrieving username
* Better unicode support for Python 3 (thanks to `astagi <https://github.com/astagi>`_)
* Add Creative Commons licenese (thanks to `rjnienaber <https://github.com/rjnienaber>`_)

**0.2**

* Add AGPL 3 license
* Add extra templates variables to GPL 2 and 3

**0.1**

* Initial release
