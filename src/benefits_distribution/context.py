from dataclasses import dataclass

@dataclass(frozen=True)
class RepositoryContext:
    repository: str
    repository_description: str
    engineering_statement: str

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
    lane_caption: str

    construction_sequence: tuple[str, ...]

    next_notebook: str
    source: str = ""
    notes: str = ""
