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
