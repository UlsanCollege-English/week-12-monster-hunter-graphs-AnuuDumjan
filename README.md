# Week 12: Monster Hunter Graphs

## Student

Name: Anu Dumjan

Student ID:2412096

## Summary

This assignment builds graph helper functions using Python.
The graph represents monster locations and routes between them.
I created both unweighted and weighted graphs using dictionaries.
The routes connect locations in both directions.
The hardest function was the weighted graph because it needed to keep the lowest danger score.

## Approach

- `build_hunter_map`:
  Used a dictionary with lists to create an undirected adjacency list.

- `build_weighted_hunter_map`:
  Used nested dictionaries to store weighted routes and checked for invalid danger scores.

- `map_summary`:
  Counted the number of locations and divided total connections by two to avoid duplicate route counting.

- `most_connected_location`:
  Compared neighbor counts and returned the alphabetically first location during ties.

- `priority_hunt_order`:
  Used heapq to sort reports from most urgent to least urgent.

## Complexity

### `build_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why:
  Each edge is processed once and stored in the graph.

### `build_weighted_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why:
  Each weighted route is added once in both directions.

### `map_summary`

- Time: O(V + E)
- Space: O(1)
- Why:
  The function loops through all graph connections.

### `most_connected_location`

- Time: O(V)
- Space: O(1)
- Why:
  It checks each location once.

### `priority_hunt_order`

- Time: O(n log n)
- Space: O(n)
- Why:
  Heap operations take log n time for each insertion and removal.

## Edge-Case Checklist

- [x] Empty graph
- [x] One route
- [x] Duplicate routes
- [x] Disconnected locations
- [x] Tie for most connected location
- [x] Positive weighted routes
- [x] Invalid zero or negative danger score
- [x] Empty priority report list

## Tests

Paste the result of your test run.

```bash
pytest -q