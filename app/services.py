import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Tuple

from .models import PathEntry, VehicleState
from .redis_client import get_redis


async def fetch_vehicle_states() -> List[VehicleState]:
    client = get_redis()
    keys = await client.keys("RGV:State:*")
    if not keys:
        return []
    values = await asyncio.gather(*(client.get(key) for key in keys))
    states = []
    for value in values:
        if not value:
            continue
        try:
            data = json.loads(value)
            states.append(VehicleState.from_dict(data))
        except json.JSONDecodeError:
            continue
    return states


async def fetch_paths() -> List[PathEntry]:
    client = get_redis()
    keys = await client.keys("Path:List:*")
    paths: List[PathEntry] = []
    for key in keys:
        entries = await client.zrange(key, 0, -1)
        for entry in entries:
            try:
                data = json.loads(entry)
                paths.append(PathEntry.from_dict(data))
            except json.JSONDecodeError:
                continue
    return paths


def calculate_congestion(
    states: List[VehicleState], paths: List[PathEntry]
) -> List[Dict[str, int]]:
    """Calculate congestion index for each grid cell.

    Returns list of dictionaries with row, col and congestion count.
    """
    counts: Dict[Tuple[int, int], int] = defaultdict(int)

    for state in states:
        counts[(state.row, state.col)] += 1
        counts[(state.target_row, state.target_col)] += 1

    for path in paths:
        counts[(path.row, path.col)] += 1

    congestion = []
    for (row, col), count in counts.items():
        if count > 1:
            congestion.append({"row": row, "col": col, "count": count})
    return congestion
