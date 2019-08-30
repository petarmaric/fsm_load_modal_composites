About
=====

Python library that loads modal composites from the file containing the
parametric model of buckling and free vibration in prismatic shell structures,
as computed by the `fsm_eigenvalue project`_.

This work is a part of the investigation within the research project
[ON174027]_, supported by the Ministry for Science and Technology, Republic of
Serbia. This support is gratefully acknowledged.

References
----------

.. [ON174027]
   "Computational Mechanics in Structural Engineering"

.. _`fsm_eigenvalue project`: https://github.com/petarmaric/fsm_eigenvalue

Installation
============

To install fsm_load_modal_composites run::

    $ pip install fsm_load_modal_composites

Usage examples
==============

Quick start::

    >>> import logging
    >>> logging.basicConfig(level=logging.DEBUG)

    >>> from pprint import pprint
    >>> from fsm_load_modal_composites import load_modal_composites

    >>> results_file = 'examples/barbero-viscoelastic.hdf5'
    >>> modal_composites, column_units, column_descriptions = load_modal_composites(
    ...     results_file, a_max=600, t_b_min=6.0
    ... )

    >>> modal_composites.shape
    (143,)

    >>> pprint(modal_composites.dtype)
    [('a', '<f8'),
     ('t_b', '<f8'),
     ('m_dominant', '<i4'),
     ('omega', '<f8'),
     ('omega_approx', '<f8'),
     ('omega_rel_err', '<f8'),
     ('sigma_cr', '<f8'),
     ('sigma_cr_approx', '<f8'),
     ('sigma_cr_rel_err', '<f8')]

     >>> pprint(column_descriptions)
     {'a': 'strip length',
      'm_dominant': 'dominant mode, modal composite via sigma_cr',
      'omega': 'natural frequency',
      'omega_approx': 'natural frequency approximated from critical buckling stress',
      'omega_rel_err': 'natural frequency relative approximation error',
      'sigma_cr': 'critical buckling stress',
      'sigma_cr_approx': 'critical buckling stress approximated from natural frequency',
      'sigma_cr_rel_err': 'critical buckling stress relative approximation error',
      't_b': 'base strip thickness'}

Please see the `fsm_modal_analysis`_ source code for more examples.

.. _`fsm_modal_analysis`: https://github.com/petarmaric/fsm_modal_analysis

Contribute
==========

If you find any bugs, or wish to propose new features `please let us know`_.

If you'd like to contribute, simply fork `the repository`_, commit your changes
and send a pull request. Make sure you add yourself to `AUTHORS`_.

.. _`please let us know`: https://github.com/petarmaric/fsm_load_modal_composites/issues/new
.. _`the repository`: https://github.com/petarmaric/fsm_load_modal_composites
.. _`AUTHORS`: https://github.com/petarmaric/fsm_load_modal_composites/blob/master/AUTHORS
