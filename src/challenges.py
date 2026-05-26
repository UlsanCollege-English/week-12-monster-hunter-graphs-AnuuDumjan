"""Week 12: Monster Hunter Graphs.

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs."""
    
    graph = {}

    for start, end in edges:
        if start not in graph:
            graph[start] = []

        if end not in graph:
            graph[end] = []

        if end not in graph[start]:
            graph[start].append(end)

        if start not in graph[end]:
            graph[end].append(start)

    return graph


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples."""

    graph = {}

    for start, end, danger in edges:

        if danger <= 0:
            raise ValueError("Danger score must be positive")

        if start not in graph:
            graph[start] = {}

        if end not in graph:
            graph[end] = {}

        if end not in graph[start] or danger < graph[start][end]:
            graph[start][end] = danger
            graph[end][start] = danger

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes."""

    locations = len(graph)

    total_routes = 0

    for neighbors in graph.values():
        total_routes += len(neighbors)

    routes = total_routes // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors."""

    if not graph:
        return None

    return min(
        graph,
        key=lambda location: (-len(graph[location]), location)
    )


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent."""

    heap = []

    for report in reports:
        heapq.heappush(heap, report)

    order = []

    while heap:
        priority, location = heapq.heappop(heap)
        order.append(location)

    return order