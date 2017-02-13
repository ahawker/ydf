"""
    ydf/registry
    ~~~~~~~~~~~~

    Registry for storing instruction type handler functions.
"""

import collections

from ydf import handlers, log


__all__ = ['global_registry']


class Registry:
    """
    Automatically discovers type handler functions for all instruction types which implement
    the :class:`~ydf.instructions.InstructionsMeta` metaclass.
    """

    def __init__(self, logger=None):
        """
        Create a new :class:`~ydf.registry.Registry` instance.

        :param logger: (Optional) logger instance to use.
        """
        self.registry = collections.defaultdict(dict)
        self.logger = logger or log.get_logger(__name__)

    def is_registered(self, instruction_name):
        """
        Check to see if the given instruction has already been registered.

        :param instruction_name: Name of the instruction to check.
        :return: `true` if the instruction is registered and `false` otherwise.
        """
        return bool(self.registry[instruction_name])

    def register(self, instruction_name, instruction_cls):
        """
        Register all discovered type handler functions in the given class attribute dict for the given
        instruction.

        :param instruction_name: Name of the instruction to register.
        :param instruction_cls: Instance of a class to examine, looking for registered type handler functions.
        :return: `None`
        """
        for handler_type, handler_func in handlers.get_type_handlers(instruction_cls).items():
            self.registry[instruction_name][handler_type] = handler_func
            self.logger.debug('Registered handler for instruction={} type={}'.format(instruction_name,
                                                                                     handler_type.__name__))


#: Default type handler registry used by :class:`~ydf.instructions.InstructionsMeta` to
#: track all instruction type handler functions.
global_registry = Registry()
