======
surgen
======

Surgen is a tool and library to help perform automated upgrades to codebases. It's goals are:

* provide a simple CLI to facilitate upgrading codebases
* provide libraries to allow easy authoring of code migration scripts.

------------
Installation
------------

`pip install surgen`



-----
Usage
-----

Surgen is available as a command line tool, providing the directory
containing surgen scripts, and the directory to apply them to:

.. code-block:: bash

    surgen ./my_upgrade_scripts ./my_target_directory

Both arguments are optional, and default to the ./surgen-scripts
directory and the current working directory, respectively.

Surgen Script
=============

A surgen script MUST contain a class that:

    * extends surgen.Procedure
    * overrides operate(self)
    * does NOT override __init__

A surgen script can:

    * provide a should_run function to determine if the script should run (default true)


Examples of surgen scripts can be found in the examples/ directory.

----
TODO
----

* backup / restore
