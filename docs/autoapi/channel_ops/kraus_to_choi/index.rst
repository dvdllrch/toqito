channel_ops.kraus_to_choi
=========================

.. py:module:: channel_ops.kraus_to_choi

.. autoapi-nested-parse::

   Computes the Choi matrix of a list of Kraus operators.



Functions
---------

.. autoapisummary::

   channel_ops.kraus_to_choi.kraus_to_choi


Module Contents
---------------

.. py:function:: kraus_to_choi(kraus_ops, sys = 2)

   Compute the Choi matrix of a list of Kraus operators.

   (Section: Kraus Representations of :cite:`Watrous_2018_TQI`).

   The Choi matrix of the list of Kraus operators, :code:`kraus_ops`. The default convention is
   that the Choi matrix is the result of applying the map to the second subsystem of the
   standard maximally entangled (unnormalized) state. The Kraus operators are expected to be
   input as a list of numpy arrays (i.e. [[:math:`A_1`, :math:`B_1`],...,[:math:`A_n`, :math:`B_n`]]).
   In case the map is CP (completely positive), it suffices to input a flat list of operators omitting
   their conjugate transpose (i.e. [:math:`K_1`,..., :math:`K_n`]).

   This function was adapted from the QETLAB package.

   .. rubric:: Examples

   The transpose map:

   The Choi matrix of the transpose map is the swap operator. Notice that the transpose map
   is *not* completely positive.

   >>> import numpy as np
   >>> from toqito.channel_ops import kraus_to_choi
   >>> kraus_1 = np.array([[1, 0], [0, 0]])
   >>> kraus_2 = np.array([[1, 0], [0, 0]]).conj().T
   >>> kraus_3 = np.array([[0, 1], [0, 0]])
   >>> kraus_4 = np.array([[0, 1], [0, 0]]).conj().T
   >>> kraus_5 = np.array([[0, 0], [1, 0]])
   >>> kraus_6 = np.array([[0, 0], [1, 0]]).conj().T
   >>> kraus_7 = np.array([[0, 0], [0, 1]])
   >>> kraus_8 = np.array([[0, 0], [0, 1]]).conj().T
   >>>
   >>> kraus_ops = [[kraus_1, kraus_2], [kraus_3, kraus_4], [kraus_5, kraus_6], [kraus_7, kraus_8]]
   >>> kraus_to_choi(kraus_ops)
   array([[1., 0., 0., 0.],
          [0., 0., 1., 0.],
          [0., 1., 0., 0.],
          [0., 0., 0., 1.]])

   .. seealso:: :func:`.choi_to_kraus`

   .. rubric:: References

   .. bibliography::
       :filter: docname in docnames

   :param kraus_ops: A list of Kraus operators.
   :param sys: The dimension of the system (default is 2).
   :return: The corresponding Choi matrix of the provided Kraus operators.



