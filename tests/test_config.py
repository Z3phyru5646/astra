from dataclasses import FrozenInstanceError

import pytest

from astra.config import RuntimeConfig


def test_runtime_config_has_expected_defaults() -> None:
    config = RuntimeConfig()

    assert config.device == "auto"
    assert config.dtype == "auto"
    assert config.seed == 42


def test_runtime_config_accepts_explicit_values() -> None:
    config = RuntimeConfig(
        device="cuda",
        dtype="float16",
        seed=123,
    )

    assert config.device == "cuda"
    assert config.dtype == "float16"
    assert config.seed == 123


def test_runtime_config_rejects_empty_device() -> None:
    with pytest.raises(ValueError, match="device must be a non-empty string"):
        RuntimeConfig(device="")


def test_runtime_config_rejects_unsupported_dtype() -> None:
    with pytest.raises(ValueError, match="Unsupported dtype"):
        RuntimeConfig(dtype="float8")


def test_runtime_config_rejects_negative_seed() -> None:
    with pytest.raises(ValueError, match="seed must be non-negative"):
        RuntimeConfig(seed=-1)


def test_runtime_config_is_immutable() -> None:
    config = RuntimeConfig()

    with pytest.raises(FrozenInstanceError):
        config.device = "cuda"  # type: ignore[misc]