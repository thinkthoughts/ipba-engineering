from __future__ import annotations

from .context import RepositoryContext


class ContextValidationError(ValueError):
    """Raised when a repository context is incomplete or inconsistent."""


def validate_context(context: RepositoryContext) -> None:
    scalar_fields = {
        "repository": context.repository,
        "repository_description": context.repository_description,
        "engineering_statement": context.engineering_statement,
        "constraint": context.constraint,
        "connected_lane": context.connected_lane,
        "repository_variable_title": context.repository_variable_title,
        "lane_caption": context.lane_caption,
        "next_notebook": context.next_notebook,
    }

    for name, value in scalar_fields.items():
        if not value.strip():
            raise ContextValidationError(
                f"{name} must be non-empty"
            )

    sequence_fields = {
        "grammar": context.grammar,
        "engineering_objects": context.engineering_objects,
        "engineering_variables": context.engineering_variables,
        "observable_states": context.observable_states,
        "indicators": context.indicators,
        "lane_symbols": context.lane_symbols,
        "lane_labels": context.lane_labels,
        "construction_sequence": context.construction_sequence,
    }

    for name, values in sequence_fields.items():
        if not values:
            raise ContextValidationError(
                f"{name} must contain at least one item"
            )

        if any(not str(item).strip() for item in values):
            raise ContextValidationError(
                f"{name} contains an empty item"
            )

    if len(context.lane_symbols) != len(context.lane_labels):
        raise ContextValidationError(
            "lane_symbols and lane_labels must have equal length"
        )

    expected_next = context.construction_sequence[1]
    expected_number = expected_next.split(" ", 1)[0]

    if not context.next_notebook.startswith(expected_number):
        raise ContextValidationError(
            "next_notebook does not match the second item "
            "in construction_sequence"
        )
