import pytest
from src.tdd_gcd_tutorial.gcd1 import gcd1
from src.tdd_gcd_tutorial.gcd2 import gcd2
from src.tdd_gcd_tutorial.gcd3 import gcd3
from src.tdd_gcd_tutorial.gcd4 import gcd4
from src.tdd_gcd_tutorial.gcd5 import gcd5
from src.tdd_gcd_tutorial.gcd6 import gcd6
from src.tdd_gcd_tutorial.gcd7 import gcd7
from src.tdd_gcd_tutorial.gcd8 import gcd8

tests = [
    (1, 1, 1),   # a = b & gcd = 1
    (3, 1, 1),   # a > b & gcd = 1
    (24, 8, 8),  # a > b & gcd > 1
    (8, 24, 8),  # a < b & gcd > 1
    (24, 16, 8), # a > b & gcd > 1
    (24, 7, 1),  # a > b & gcd = 1
]

@pytest.mark.parametrize("a,b,expected", tests)
@pytest.mark.parametrize(
    "func",
    [
        pytest.param(gcd1, id="gcd1"),
        pytest.param(gcd2, id="gcd2"),
        pytest.param(gcd3, id="gcd3"),
        pytest.param(gcd4, id="gcd4"),
        pytest.param(gcd5, id="gcd5"),
        pytest.param(gcd6, id="gcd6"),
        pytest.param(gcd7, id="gcd7"),
        pytest.param(gcd8, id="gcd8"),
    ],
)
def test_gcd(func, a, b, expected):
    assert func(a, b) == expected

# test execution
# pytest tests/tdd_gcd_tutorial/test_gcd.py -v -s

# results:
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd1-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd1-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd1-24-8-8] FAILED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd1-8-24-8] FAILED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd1-24-16-8] FAILED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd1-24-7-1] PASSED

# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd2-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd2-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd2-24-8-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd2-8-24-8] FAILED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd2-24-16-8] FAILED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd2-24-7-1] FAILED

# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd3-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd3-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd3-24-8-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd3-8-24-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd3-24-16-8] FAILED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd3-24-7-1] FAILED

# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd4-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd4-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd4-24-8-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd4-8-24-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd4-24-16-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd4-24-7-1] FAILED

# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd5-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd5-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd5-24-8-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd5-8-24-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd5-24-16-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd5-24-7-1] PASSED

# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd6-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd6-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd6-24-8-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd6-8-24-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd6-24-16-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd6-24-7-1] PASSED

# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd7-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd7-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd7-24-8-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd7-8-24-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd7-24-16-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd7-24-7-1] PASSED

# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd8-1-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd8-3-1-1] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd8-24-8-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd8-8-24-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd8-24-16-8] PASSED
# tests/tdd_gcd_tutorial/test_gcd.py::test_gcd[gcd8-24-7-1] PASSED