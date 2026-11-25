# 14 - Intervals

## Pattern Cues ("If you see X, think Y")
- **Merge overlapping intervals / insert interval:** Sort by `start` (`intervals.sort(key=lambda x: x[0])`), then compare `cur_start <= prev_end` and merge via `prev_end = max(prev_end, cur_end)`.
- **Minimum removals to eliminate overlaps (`Non-overlapping Intervals`):** Sort by `end` time (or sort by `start` and upon overlap keep the interval with the **smaller end**).
- **Minimum concurrent rooms / peak overlap (`Meeting Rooms II`):** Sort start times and end times separately (two pointers) or use a Min-Heap of active `end` times.

## Core Python Template
```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

## Complexity & Pitfalls
- **Time:** $O(n \log n)$ dominated by sorting.
- **Space:** $O(n)$ for the output (or heap).
- **Pitfalls:**
  - Clarify whether touching endpoints `[1, 2]` and `[2, 3]` count as overlapping (`Merge Intervals`: yes, `start <= prev_end`; `Meeting Rooms`: no, `start < prev_end`).

## Target Problems (NeetCode 150)
- `0057` Insert Interval (Medium) *
- `0056` Merge Intervals (Medium) *
- `0435` Non-overlapping Intervals (Medium) *
- `0252` Meeting Rooms (Easy) *
- `0253` Meeting Rooms II (Medium) *
- `1851` Minimum Interval to Include Each Query (Hard)
