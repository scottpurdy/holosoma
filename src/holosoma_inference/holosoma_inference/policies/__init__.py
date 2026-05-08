from .base import BasePolicy
from .dual_mode import DualModePolicy
from .locomotion import LocomotionPolicy

__all__ = ["BasePolicy", "DualModePolicy", "LocomotionPolicy", "WholeBodyTrackingPolicy"]


def __getattr__(name):
    if name == "WholeBodyTrackingPolicy":
        from .wbt import WholeBodyTrackingPolicy

        return WholeBodyTrackingPolicy
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
