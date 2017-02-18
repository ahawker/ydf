"""
    test_formatting
    ~~~~~~~~~~~~~~~

    Tests for the :mod:`~ydf.formatting` module.
"""

import pytest

from ydf import formatting


@pytest.fixture(scope='module', params=[
    ['foo'],
    ['bar'],
    ['baz']
])
def one_item_list(request):
    """
    Fixture that yields one item lists.
    """
    return request.param


@pytest.fixture(scope='module', params=[
    ['foo', 'bar'],
    ['foo', 'bar', 'baz'],
    ['foo', 'bar', 'baz', 'jaz'],
    ['foo', 'bar', 'baz', 'jaz', 'faz'],
    ['foo', 'bar', 'baz', 'jaz', 'faz', 'zaz']
])
def multi_item_list(request):
    """
    Fixture that yields multi item lists.
    """
    return request.param


@pytest.fixture(scope='module', params=[
    dict(name='foo'),
    dict(foo='bar'),
    dict(bar='baz')
])
def one_item_dict(request):
    """
    Fixture that yields one item dicts.
    """
    return request.param


@pytest.fixture(scope='module', params=[
    dict(foo='foo'),
    dict(foo='foo', bar='bar'),
    dict(foo='foo', bar='bar', baz='baz'),
    dict(foo='foo', bar='bar', baz='baz', jaz='jaz'),
    dict(foo='foo', bar='bar', baz='baz', jaz='jaz', faz='faz'),
    dict(foo='foo', bar='bar', baz='baz', jaz='jaz', faz='faz', zaz='zaz')
])
def multi_item_dict(request):
    """
    Fixture that yields multi item dicts.
    """
    return request.param


def test_list_doesnt_line_break_on_single_item(one_item_list):
    """
    Assert that :func:`~ydf.formatting.list_with_conditional_line_breaks` doesn't insert a line break
    for lists with only one item.
    """
    assert formatting.list_with_conditional_line_breaks(one_item_list) == one_item_list[0]


def test_list_uses_given_line_break(multi_item_list):
    """
    Assert that :func:`~ydf.formatting.list_with_conditional_line_breaks` uses the given line break
    string as expected.
    """
    line_break = '$'
    expected = '{}{}'.format(line_break, ' ' * formatting.DEFAULT_INDENT).join(multi_item_list)
    assert formatting.list_with_conditional_line_breaks(multi_item_list, line_break) == expected


def test_list_uses_given_indentation(multi_item_list):
    """
    Assert that :func:`~ydf.formatting.list_with_conditional_line_breaks` uses the given indentation size
    as expected.
    """
    indent = 2
    expected = '{}{}'.format(formatting.DEFAULT_LINE_BREAK, ' ' * indent).join(multi_item_list)
    assert formatting.list_with_conditional_line_breaks(multi_item_list, indent=indent) == expected


def test_dict_doesnt_line_break_on_single_item(one_item_dict):
    """
    Assert that :func:`~ydf.formatting.dict_with_conditional_line_breaks` doesn't insert a line break
    for dicts with only one item.
    """
    kvp = list(one_item_dict.items())[0]
    assert formatting.dict_with_conditional_line_breaks(one_item_dict) == '{}={}'.format(*kvp)
