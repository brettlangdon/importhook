Importhook
=========

.. image:: https://badge.fury.io/py/importhook.svg
    :target: https://badge.fury.io/py/importhook


Installation
~~~~~~~~~~~~

.. code:: bash

   pip install importhook


Usage
~~~~~

.. code:: python

   import importhook

   # Setup hook to be called any time the `socket` module is imported and loaded into module cache
   @importhook.on_import('socket')
   def on_socket_import(socket):
       print('"socket" module has been imported')

   # Import module
   import socket
