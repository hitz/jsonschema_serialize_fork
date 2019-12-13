"""
An implementation of JSON Schema for Python

The main functionality is provided by the validator classes for each of the
supported JSON Schema versions.

Most commonly, `validate` is the quickest way to simply validate a given
instance under a schema, and will create a validator for you.
"""

from jsonschema_serialize_fork.exceptions import (
    ErrorTree, FormatError, RefResolutionError, SchemaError, ValidationError
)
from jsonschema_serialize_fork._format import (
    FormatChecker,
    draft3_format_checker,
    draft4_format_checker,
    draft6_format_checker,
    draft7_format_checker,
)
from jsonschema_serialize_fork._types import TypeChecker
from jsonschema_serialize_fork.validators import (
    Draft3Validator,
    Draft4Validator,
    Draft6Validator,
    Draft7Validator,
    RefResolver,
    validate,
    ErrorTree,
    serialize,
)
from jsonschema_serialize_fork._serializers import NO_DEFAULT

try:
    from importlib import metadata
except ImportError: # for Python<3.8
    import importlib_metadata as metadata
__version__ = metadata.version("jsonschema_serialize_fork")