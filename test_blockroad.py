# test_blockroad.py
"""
Tests for BlockRoad module.
"""

import unittest
from blockroad import BlockRoad

class TestBlockRoad(unittest.TestCase):
    """Test cases for BlockRoad class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockRoad()
        self.assertIsInstance(instance, BlockRoad)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockRoad()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
