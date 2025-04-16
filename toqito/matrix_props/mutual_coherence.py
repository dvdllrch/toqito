"""Computes the mutual coherence for a list of 1D numpy arrays."""

import numpy as np


def mutual_coherence(setofvecs: list[np.ndarray]) -> float:
    r"""Calculate the mutual coherence of a set of vectors.

    The mutual coherence of a set of vectors is defined as the maximum absolute
    value of the inner product between any two distinct vectors, divided by the
    product of their norms :cite:WikiMutualCoh. It provides a measure of how
    similar the vectors are to each other.

    Examples
    =======
    >>> import numpy as np
    >>> from toqito.matrix_props.mutual_coherence import mutual_coherence
    >>> example_A = [np.array([1, 0]), np.array([0, 1])]
    >>> mutual_coherence(example_A)
    0.0

    >>> # An example with a larger set of vectors
    >>> example_B = [np.array([1, 0, 1]), np.array([0, 1, 1]), np.array([1, 1, 0])]
    >>> mutual_coherence(example_B)
    0.5

    References
    ==========
    .. bibliography::
        :filter: docname in docnames

    :param states: A list of 1D numpy arrays.
    :raises isinstance: Check if input is valid.
    :return: The mutual coherence.

    """
    # Check if the input is a valid list of 1D numpy arrays.
    if not isinstance(setofvecs, list):
        raise TypeError("Input must be a list of 1D numpy arrays.")
    if not all(isinstance(vec, np.ndarray) and vec.ndim == 1 for vec in setofvecs):
        raise ValueError("All elements in the list must be 1D numpy arrays.")

    # Convert input into a 2D numpy array.
    setofvecs = np.column_stack(setofvecs).astype(float)

    # Normalize the the vectors.
    setofvecs /= np.linalg.norm(setofvecs, axis=0)

    # Calculate the inner product between all pairs of columns.
    inner_products = np.abs(np.conj(setofvecs.T) @ setofvecs)

    # Set diagonal elements to zero (only respecting distinct vectors).
    np.fill_diagonal(inner_products, 0)

    return inner_products.max()
