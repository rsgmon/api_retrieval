===============================
API Retrieval
===============================


.. image:: https://img.shields.io/pypi/v/api_retrieval.svg
        :target: https://pypi.python.org/pypi/api_retrieval

.. image:: https://img.shields.io/travis/rsgmon/api_retrieval.svg
        :target: https://travis-ci.org/rsgmon/api_retrieval

.. image:: https://readthedocs.org/projects/api-retrieval/badge/?version=latest
        :target: https://api-retrieval.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/rsgmon/api_retrieval/shield.svg
     :target: https://pyup.io/repos/github/rsgmon/api_retrieval/
     :alt: Updates


Configrable ETL CLI App


* Free software: BSD license
* Documentation: https://api-retrieval.readthedocs.io.


Features
--------

Query any REST API by creating a JSON file that specifies the post request you want.

If you want to simply print out the results of an API call this can be done directly from the the command line.

example:
python [path_to_main]\main.py path_to_your_json_config_file

If you want to incorporate the results in another program start with the config module. You instantiate a config object with a python object and then send to an http_request object.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

