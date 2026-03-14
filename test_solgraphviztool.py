# test_solgraphviztool.py
"""
Tests for SolgraphVizTool module.
"""

import unittest
from solgraphviztool import SolgraphVizTool

class TestSolgraphVizTool(unittest.TestCase):
    """Test cases for SolgraphVizTool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolgraphVizTool()
        self.assertIsInstance(instance, SolgraphVizTool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolgraphVizTool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
