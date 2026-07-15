"""Core runtime kernel for ASTRA."""

from enum import Enum, auto


class KernelState(Enum):
    """Lifecycle states of the ASTRA runtime kernel."""

    CREATED = auto()
    RUNNING = auto()
    STOPPED = auto()


class RuntimeKernel:
    """Coordinates the lifecycle of the ASTRA runtime."""

    def __init__(self) -> None:
        self._state = KernelState.CREATED

    @property
    def state(self) -> KernelState:
        """Return the current kernel lifecycle state."""
        return self._state

    def start(self) -> None:
        """Start the runtime kernel."""
        if self._state is not KernelState.CREATED:
            raise RuntimeError(
                f"Cannot start kernel from state {self._state.name}."
            )

        self._state = KernelState.RUNNING

    def stop(self) -> None:
        """Stop the runtime kernel."""
        if self._state is not KernelState.RUNNING:
            raise RuntimeError(
                f"Cannot stop kernel from state {self._state.name}."
            )

        self._state = KernelState.STOPPED