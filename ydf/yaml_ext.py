"""
    ydf/yaml_ext
    ~~~~~~~~~~~~

    Contains extensions to existing YAML functionality.
"""

import collections

from ruamel import yaml
from ruamel.yaml import resolver


class OrderedLoader(yaml.Loader):
    """
    Extends the default YAML loader to use :class:`~collections.OrderedDict` for mapping
    types.
    """

    def __init__(self, *args, **kwargs):
        super(OrderedLoader, self).__init__(*args, **kwargs)
        self.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, self.construct_ordered_mapping)

    @staticmethod
    def construct_ordered_mapping(loader, node):
        loader.flatten_mapping(node)
        return collections.OrderedDict(loader.construct_pairs(node))


def load(stream):
    """
    Load the given YAML string.
    """
    return yaml.load(stream, OrderedLoader)
