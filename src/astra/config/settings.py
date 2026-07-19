"""Runtime configuration for ASTRA."""

from dataclasses import dataclass


SUPPORTED_DTYPES = frozenset({"auto", "float32", "float16", "bfloat16"})


@dataclass(frozen=True, slots=True)
class RuntimeConfig:
    """Core configuration for an ASTRA runtime instance."""

    device: str = "auto"
    dtype: str = "auto"
    seed: int = 42

    def __post_init__(self) -> None:
        if not self.device:
            raise ValueError("device must be a non-empty string.")

        if self.dtype not in SUPPORTED_DTYPES:
            supported = ", ".join(sorted(SUPPORTED_DTYPES))
            raise ValueError(
                f"Unsupported dtype {self.dtype!r}. "
                f"Supported values: {supported}."
            )

        if self.seed < 0:
            raise ValueError("seed must be non-negative.")