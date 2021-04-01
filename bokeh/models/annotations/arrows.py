#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
'''

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from ...core.enums import SpatialUnits
from ...core.has_props import abstract
from ...core.properties import (
    Bool,
    Enum,
    Include,
    Instance,
    Nullable,
    NumberSpec,
    Override,
    field,
)
from ...core.property_mixins import FillProps, LineProps
from ..graphics import Marking
from .annotation import DataAnnotation

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    "Arrow",
    "ArrowHead",
    "NormalHead",
    "OpenHead",
    "TeeHead",
    "VeeHead",
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

@abstract
class ArrowHead(Marking):
    ''' Base class for arrow heads.

    '''

    size = NumberSpec(default=25, help="""
    The size, in pixels, of the arrow head.
    """)

    reversed = Bool(default=False)

class OpenHead(ArrowHead):
    ''' Render an open-body arrow head.

    '''

    line_props = Include(LineProps, help="""

    The {prop} values for the arrow head outline.
    """)

class NormalHead(ArrowHead):
    ''' Render a closed-body arrow head.

    '''

    line_props = Include(LineProps, help="""
    The {prop} values for the arrow head outline.
    """)

    fill_props = Include(FillProps, help="""
    The {prop} values for the arrow head interior.
    """)

    fill_color = Override(default="black")

class TeeHead(ArrowHead):
    ''' Render a tee-style arrow head.

    '''

    line_props = Include(LineProps, help="""
    The {prop} values for the arrow head outline.
    """)

class VeeHead(ArrowHead):
    ''' Render a vee-style arrow head.

    '''

    line_props = Include(LineProps, help="""
    The {prop} values for the arrow head outline.
    """)

    fill_props = Include(FillProps, help="""
    The {prop} values for the arrow head interior.
    """)

    fill_color = Override(default="black")

class Arrow(DataAnnotation):
    ''' Render arrows as an annotation.

    See :ref:`userguide_annotations_arrows` for information on plotting arrows.

    '''

    x_start = NumberSpec(default=field("x_start"), help="""
    The x-coordinates to locate the start of the arrows.
    """)

    y_start = NumberSpec(default=field("y_start"), help="""
    The y-coordinates to locate the start of the arrows.
    """)

    start_units = Enum(SpatialUnits, default='data', help="""
    The unit type for the start_x and start_y attributes. Interpreted as "data
    space" units by default.
    """)

    start = Nullable(Instance(ArrowHead), help="""
    Instance of ``ArrowHead``.
    """)

    x_end = NumberSpec(default=field("x_end"), help="""
    The x-coordinates to locate the end of the arrows.
    """)

    y_end = NumberSpec(default=field("y_end"), help="""
    The y-coordinates to locate the end of the arrows.
    """)

    end_units = Enum(SpatialUnits, default='data', help="""
    The unit type for the end_x and end_y attributes. Interpreted as "data
    space" units by default.
    """)

    end = Nullable(Instance(ArrowHead), default=lambda: OpenHead(), help="""
    Instance of ``ArrowHead``.
    """)

    body_props = Include(LineProps, help="""
    The {prop} values for the arrow body.
    """)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
