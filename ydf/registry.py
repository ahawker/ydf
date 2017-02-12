"""
    ydf/registry
    ~~~~~~~~~~~~

    Registry for storing instruction type handler functions.
"""

import collections
import re

from ydf import log


__all__ = ['global_registry']


class Registry:
    """
    Automatically discovers type handler functions for all instruction types which implement
    the :class:`~ydf.instructions.InstructionsMeta` metaclass.
    """

    def __init__(self, pattern='^from_(\w+)$', logger=None):
        """
        Create a new :class:`~ydf.registry.Registry` instance.

        :param pattern: (Optional) regex pattern for finding type handler class functions.
        :param logger: (Optional) logger instance to use.
        """
        self.registry = collections.defaultdict(dict)
        self.pattern = re.compile(pattern, re.IGNORECASE)
        self.logger = logger or log.get_logger(__name__)

    def is_registered(self, instruction_name):
        """
        Check to see if the given instruction has already been registered.

        :param instruction_name: Name of the instruction to check.
        :return: `true` if the instruction is registered and `false` otherwise.
        """
        return bool(self.registry[instruction_name])

    def register(self, instruction_name, attrs):
        """
        Register all discovered type handler functions in the given class attribute dict for the given
        instruction.

        :param instruction_name: Name of the instruction to register.
        :param attrs: Dict of class attributes to check for type handlers
        :return: `None`
        """
        for name, func in attrs.items():
            match = self.pattern.match(name)
            if not match:
                continue
            func_type = match.group(1)
            self.logger.debug('Registering {} type handler for {}'.format(func_type, instruction_name))
            self.registry[instruction_name][func_type] = func


#: Default type handler registry used by :class:`~ydf.instructions.InstructionsMeta` to
#: track all instruction type handler functions.
global_registry = Registry()
