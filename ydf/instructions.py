"""
    ydf/instructions
    ~~~~~~~~~~~~~~~~

    Convert objects parsed from YAML to those that represent Dockerfile instructions.
"""

__all__ = []


FROM = 'FROM'
RUN = 'RUN'
CMD = 'CMD'
LABEL = 'LABEL'
EXPOSE = 'EXPOSE'
ENV = 'ENV'
ADD = 'ADD'
COPY = 'COPY'
ENTRYPOINT = 'ENTRYPOINT'
VOLUME = 'VOLUME'
USER = 'USER'
WORKDIR = 'WORKDIR'
ARG = 'ARG'
ONBUILD = 'ONBUILD'
STOPSIGNAL = 'STOPSIGNAL'
HEALTHCHECK = 'HEALTHCHECK'
SHELL = 'SHELL'
