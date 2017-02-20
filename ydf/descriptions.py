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

LABEL_DICT = '{"key1": "value1", "key2": "value2"}'

EXPOSE_INT = '<port>'
EXPOSE_LIST = '<port> <port> <port>'

ENV_STR = '<key> <value>'
ENV_DICT = '<key>=<value> <key>=<value>'

ADD_STR = '<src>... <dst>'
ADD_LIST = '["<src>", ..., "<dest>"]'

COPY_STR = '<src>... <dst>'
COPY_LIST = '["<src>", ..., "<dest>"]'

ENTRYPOINT_STR = 'command param1 param2'
ENTRYPOINT_LIST = '["executable", "param1", "param2"]'
ENTRYPOINT_DICT = '{"executable": "...", "params": ["...", "..."]}'

VOLUME_STR = '<path>'
VOLUME_LIST = '["<path>", "<path>", "<path>"]'

USER_STR = '<username>'
USER_INT = '<uid>'

WORKDIR_STR = '<path>'

ARG_STR = '<name>[=<default value>]'
ARG_DICT = '{"<name>": "<default_value>"}'
