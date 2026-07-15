# ASTRA

**Adaptive Systems for Transformer Runtime Acceleration**

ASTRA is a research-oriented transformer inference runtime focused on low latency,
high throughput, efficient GPU memory utilization, and adaptive execution.

> ASTRA is currently under active development. Performance claims will only be
> published alongside reproducible benchmark configurations and results.

## Development Status

Early runtime foundation.

## Development Setup

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python -m pytest

