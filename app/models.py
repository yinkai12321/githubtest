from dataclasses import dataclass


@dataclass
class VehicleState:
    """Simplified vehicle state used for congestion calculation."""

    id: int
    row: int
    col: int
    target_row: int
    target_col: int

    @classmethod
    def from_dict(cls, data: dict) -> "VehicleState":
        return cls(
            id=data.get("Id", 0),
            row=data.get("Row", 0),
            col=data.get("Col", 0),
            target_row=data.get("TargetRow", 0),
            target_col=data.get("TargetCol", 0),
        )


@dataclass
class PathEntry:
    """A single step in a vehicle path."""

    row: int
    col: int

    @classmethod
    def from_dict(cls, data: dict) -> "PathEntry":
        return cls(row=data.get("Row", 0), col=data.get("Col", 0))
