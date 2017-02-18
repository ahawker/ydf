"""
    ydf/descriptions
    ~~~~~~~~~~~~~~~~

    Descriptions of instructions as small code examples.
"""

FROM_STR = '<image>, <image>:<tag>, or <image>@<digest>'
FROM_DICT = '{"name": "...", "tag": "...", "digest": "..."}'

RUN_STR = '<image>'
RUN_LIST = '[<executable>, <param1>, <param2>]'
RUN_DICT = '{"executable": "...", "params": ["...", "...", "..."]}'

CMD_STR = 'command param1 param2'
CMD_LIST = '["param1", "param2"]'
CMD_DICT = '{"executable": "...", "params": ["...", "..."]}'
