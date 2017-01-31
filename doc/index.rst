.. rubric:: `Beau Barker <https://bcb.github.io/>`__

jsonrpcserver
*************

Process `JSON-RPC <http://www.jsonrpc.org/>`_ requests in Python 2.7 and 3.3+.

.. code-block:: python

    from jsonrpcserver import methods

    @methods.add
    def ping():
        return 'pong'

    if __name__ == '__main__':
        methods.serve_forever()

Start the server:

.. code-block:: sh

    $ pip install jsonrpcserver
    $ python server.py
     * Listening on port 5000

This example uses the built-in server, but you can process requests in any
application with ``dispatch()``. See :doc:`examples in various frameworks
<examples>`, or read the :doc:`guide to usage and configuration <api>`.

Contribute on `Github <https://github.com/bcb/jsonrpcserver>`_.

See also: `jsonrpcclient <https://jsonrpcclient.readthedocs.io/>`_
