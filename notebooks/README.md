# Notebooks

These notebooks specify one connected stage of the engineering development of this repository.

## Repository grammar

```
Constraint
↓
Connected lanes
↓
Engineering objects
↓
Engineering variables
↓
Observable states
↓
Indicators
```

## Construction sequence

- `00_engineering_context.ipynb` — engineering context for engineering variable as an engineering variable.
- `01_constraints.ipynb` — deployment constraints and admissible engineering assumptions.
- `07_connected_lanes.ipynb` — connected deployment lanes linking policy, telemetry, engineering variable, and development indicators.
- `11_engineering_objects.ipynb` — engineering objects defined within the connected deployment lane.
- `13_engineering_variables.ipynb` — measurable engineering variables associated with those objects.
- `17_state_estimation.ipynb` — estimating observable system state from deployment telemetry.
- `19_distribution.ipynb` — engineering variable as an engineering object and measurable state.
- `23_dynamics.ipynb` — dynamics of engineering variable under deployment constraints.
- `29_optimization.ipynb` — optimization of engineering variable subject to engineering constraints.
- `37_controllers.ipynb` — controllers that regulate deployment using engineering variables and observable states.
- `43_benchmarks.ipynb` — benchmarks and indicators used to evaluate deployment strategies.

Each notebook specifies one connected stage of repository development.
