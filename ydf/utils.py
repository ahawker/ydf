"""
    ydf/utils
    ~~~~~~~~~

    Contains utility functions that have no better home.
"""


def merge_maps(*maps):
    """
    Merge the given a sequence of :class:`~collections.Mapping` instances.

    :param maps: Sequence of mapping instance to merge together.
    :return: A :class:`dict` containing all merged maps.
    """
    merged = {}
    for m in maps:
        merged.update(m)
    return merged
