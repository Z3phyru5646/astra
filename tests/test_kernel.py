import pytest

from astra.kernel import KernelState, RuntimeKernel


def test_kernel_starts_in_created_state() -> None:
    kernel = RuntimeKernel()

    assert kernel.state is KernelState.CREATED


def test_kernel_can_start() -> None:
    kernel = RuntimeKernel()

    kernel.start()

    assert kernel.state is KernelState.RUNNING


def test_kernel_can_stop_after_starting() -> None:
    kernel = RuntimeKernel()

    kernel.start()
    kernel.stop()

    assert kernel.state is KernelState.STOPPED


def test_kernel_cannot_start_twice() -> None:
    kernel = RuntimeKernel()

    kernel.start()

    with pytest.raises(RuntimeError, match="Cannot start kernel"):
        kernel.start()


def test_kernel_cannot_stop_before_starting() -> None:
    kernel = RuntimeKernel()

    with pytest.raises(RuntimeError, match="Cannot stop kernel"):
        kernel.stop()