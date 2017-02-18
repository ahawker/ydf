"""
    ydf/formatting
    ~~~~~~~~~~~~~~

    Helper functions for cleanly formatting instructions.
"""


DEFAULT_LINE_BREAK = ' \\\n'
DEFAULT_INDENT = 4
DEFAULT_QUOTE_ESCAPE = False
DEFAULT_KEY_VALUE_DELIMITER = '='
DEFAULT_STR_JOIN_DELIMITER = None


def _escape(value, escape=DEFAULT_QUOTE_ESCAPE):
    """
    Optionally double-quote escape the given string value.

    :param escape: Flag to indicate if the given string should be quote escaped.
    :return: String that is optionally escaped.
    """
    template = '"{}"' if escape else '{}'
    return template.format(value)


def _break(line_break=DEFAULT_LINE_BREAK, indent=DEFAULT_INDENT):
    """
    Build a string that represents a line break with an indentation to align with
    the previous line.

    :param line_break: String to use for a line break
    :param indent: Number of spaces to indent after the line break
    :return: String that performs a line break and indentation to align
    """
    return line_break + ' ' * indent


def _line_break_join(lst, line_break=DEFAULT_LINE_BREAK, indent=DEFAULT_INDENT):
    """
    Build a multi-line string using the given line break and alignment indentation size for
    each item in the list.

    :param lst: List of items to separate with indented line breaks
    :param line_break: String to use for each line break
    :param indent: Number of spaces for alignment indentation
    :return: Multi-line string with indented line breaks for each item
    """
    return _break(line_break, indent).join(lst)


def list_with_conditional_line_breaks(lst, line_break=DEFAULT_LINE_BREAK, indent=DEFAULT_INDENT,
                                      quote_escape=DEFAULT_QUOTE_ESCAPE):
    """
    Build a string with line breaks & indentation for lists with more than one item.

    :param lst: Collection of items to line separate
    :param line_break: String used to separate each item
    :param indent: Number of spaces used to indent each new line
    :param quote_escape: Optional flag to indicate if each item should be escaped with double quotes
    :return: Multi-line string that is well formed for human readers
    """
    return _line_break_join((_escape(v, quote_escape) for v in lst), line_break, indent)


def dict_with_conditional_line_breaks(dct, delimiter=DEFAULT_KEY_VALUE_DELIMITER, line_break=DEFAULT_LINE_BREAK,
                                      indent=DEFAULT_INDENT, quote_escape=DEFAULT_QUOTE_ESCAPE):
    """
    Build a string with line breaks & indentation for dicts with more than one item.

    :param dct: Collection of key/values to line separate
    :param delimiter: Delimiter character that should be displayed between each key/value pair
    :param line_break: String used to separate each item
    :param indent: Number of spaces used to indent each new line
    :param quote_escape: Optional flag to indicate if each key and value should be escaped with double quotes
    :return: Multi-line string that is well formed for human readers
    """
    pairs = (delimiter.join((_escape(k, quote_escape), _escape(v, quote_escape))) for k, v in dct.items())
    return _line_break_join(pairs, line_break, indent)


def str_join_with_conditional_delimiter(parts, delimiter=DEFAULT_STR_JOIN_DELIMITER):
    """
    Build a string by performing an optional join if given a iterable and delimiter.

    :param parts: String or iterable to join
    :param delimiter: (Optional) String delimiter to use for join
    :return: Original string or multi part string joined with delimiter
    """
    if isinstance(parts, str):
        return parts

    delimiter = delimiter or ''
    return delimiter.join(str(part) for part in parts if part)
