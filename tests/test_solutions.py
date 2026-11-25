"""Test suite that validates all solution files, headers, and algorithm templates.

Works with both `pytest` and standard library `python3 tests/test_solutions.py` (or `python3 -m unittest`).
"""

import importlib.util
from pathlib import Path
import re
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
PATTERNS_DIR = ROOT_DIR / "patterns"

REQUIRED_HEADER_FIELDS = (
    "Problem:",
    "URL:",
    "Difficulty:",
    "Pattern:",
    "Cue:",
    "Time Complexity:",
    "Space Complexity:",
    "Date Solved:",
    "Attempts:",
    "Hints Used:",
)


def discover_solution_files() -> list[Path]:
    return sorted(PATTERNS_DIR.glob("*/*.py"))


def validate_solution_file(sol_path: Path) -> None:
    assert re.match(r"^\d{4}-[a-z0-9-]+\.py$", sol_path.name), (
        f"Solution filename {sol_path.name} must match NNNN-kebab-case.py"
    )

    source = sol_path.read_text(encoding="utf-8")
    for field in REQUIRED_HEADER_FIELDS:
        assert field in source, f"Missing required header field '{field}' in {sol_path}"

    spec = importlib.util.spec_from_file_location(sol_path.stem.replace("-", "_"), sol_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    test_funcs = [
        getattr(module, name)
        for name in dir(module)
        if name.startswith("test_") and callable(getattr(module, name))
    ]
    assert test_funcs, f"No test_*() functions found in {sol_path}"
    for fn in test_funcs:
        fn()


def test_all_solutions() -> None:
    solutions = discover_solution_files()
    assert solutions, "No solution files found under patterns/"
    for sol_path in solutions:
        validate_solution_file(sol_path)


def test_algorithm_templates() -> None:
    if str(ROOT_DIR) not in sys.path:
        sys.path.insert(0, str(ROOT_DIR))
    from templates.algorithms import (
        Trie,
        UnionFind,
        binary_search_first_true,
        dijkstra,
        grid_bfs,
        next_greater_indices,
        sliding_window_template,
        topological_sort,
    )

    assert binary_search_first_true(1, 10, lambda x: x * x >= 30) == 6
    assert sliding_window_template([2, 1, 5, 1, 3, 2], 7) == 3
    assert next_greater_indices([2, 1, 2, 4, 3]) == [3, 2, 3, -1, -1]

    grid = [
        [0, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
    ]
    dist = grid_bfs(grid, (0, 0))
    assert dist[2][2] == 4

    order = topological_sort(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    assert order[0] == 0 and order[-1] == 3

    uf = UnionFind(4)
    assert uf.union(0, 1) is True
    assert uf.union(1, 2) is True
    assert uf.union(0, 2) is False
    assert uf.components == 2

    dists = dijkstra(3, [(0, 1, 4), (0, 2, 1), (2, 1, 2)], 0)
    assert dists == [0, 3, 1]

    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True


class InterviewPrepTestSuite(unittest.TestCase):
    def test_solutions(self) -> None:
        for sol_path in discover_solution_files():
            with self.subTest(solution=f"{sol_path.parent.name}/{sol_path.name}"):
                validate_solution_file(sol_path)

    def test_templates(self) -> None:
        test_algorithm_templates()


if __name__ == "__main__":
    unittest.main(verbosity=2)

