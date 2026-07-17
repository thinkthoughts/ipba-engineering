from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RepositoryContext:
    """Repository-specific source object for Notebook 00 artifacts."""

    repository: str
    repository_description: str

    engineering_statement_title: str
    engineering_statement: str

    grammar_title: str
    grammar: tuple[str, ...]

    constraint: str
    connected_lane: str

    engineering_objects: tuple[str, ...]
    engineering_variables: tuple[str, ...]
    observable_states: tuple[str, ...]
    indicators: tuple[str, ...]

    lane_symbols: tuple[str, ...]
    lane_labels: tuple[str, ...]

    repository_variable_title: str
    lane_relationships: tuple[str, ...]

    repository_sequence_title: str
    repository_sequence_caption: str

    construction_sequence: tuple[str, ...]

    design_principle: str
    next_notebook: str

    source: str = ""
    notes: str = ""
