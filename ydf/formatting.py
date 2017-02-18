"""
    ydf/formatting
    ~~~~~~~~~~~~~~

    Helper functions for cleanly formatting instructions.
"""


def list_with_conditional_line_breaks(lst, line_break=' \\\n', indent=4, quote_escape=False):
    """
    Build a string with line breaks & indentation for lists with more than one item.

    :param lst: Collection of items to line separate
    :param line_break: String used to separate each item
    :param indent: Number of spaces used to indent each new line
    :param quote_escape: Optional flag to indicate if each item should be escaped with double quotes
    :return: Multi-line string that is well formed for human readers
    """
    value_fmt = '"{}"' if quote_escape else '{}'
    return (line_break + ' ' * indent).join(value_fmt.format(v) for v in lst)


def dict_with_conditional_line_breaks(dct, delimiter='=', line_break=' \\\n', indent=4, quote_escape=False):
    """
    Build a string with line breaks & indentation for dicts with more than one item.

    :param dct: Collection of key/values to line separate
    :param delimiter: Delimiter character that should be displayed between each key/value pair
    :param line_break: String used to separate each item
    :param indent: Number of spaces used to indent each new line
    :param quote_escape: Optional flag to indicate if each key and value should be escaped with double quotes
    :return: Multi-line string that is well formed for human readers
    """
    key_value_fmt = '"{}"' if quote_escape else '{}'
    return (line_break + ' ' * indent).join(key_value_fmt.format(k) + delimiter + key_value_fmt.format(v)
                                            for k, v in dct.items())


def str_join_with_conditional_delimiter(parts, delimiter=None):
    """
    Build a string by performing an optional join if given a iterable and delimiter.

    :param parts: String or iterable to join
    :param delimiter: (Optional) String delimiter to use for join
    :return: Original string or multi part string joined with delimiter
    """
    if isinstance(parts, str):
        return parts

    delimiter = delimiter or ''
    return delimiter.join(part for part in parts if part)
