"""
Reusable infrastructure for benefits-distribution notebooks.
"""

from .context import RepositoryContext
from .export import finalize_notebook
from .figures import generate_context_figures
from .paths import (
    DATA,
    FIGURES,
    NOTEBOOKS,
    RESULTS,
    ROOT,
    initialize_directories,
)
from .validation import (
    ContextValidationError,
    validate_context,
)

__all__ = [
    "RepositoryContext",
    "ContextValidationError",
    "ROOT",
    "FIGURES",
    "RESULTS",
    "DATA",
    "NOTEBOOKS",
    "initialize_directories",
    "generate_context_figures",
    "validate_context",
    "finalize_notebook",
]
