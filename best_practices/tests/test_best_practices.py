"""
Unit and regression test for the best_practices package.
"""

# Import package, test suite, and other packages as needed
import best_practices
import pytest
import sys

def test_best_practices_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "best_practices" in sys.modules
