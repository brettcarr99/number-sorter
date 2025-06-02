#!/usr/bin/env python3
"""
Tests for the number sorter program using pytest
"""

import pytest
import tempfile
import os
from number_sorter import read_numbers_from_file, sort_numbers, write_numbers_to_file


class TestReadNumbersFromFile:
    """Test cases for reading numbers from file."""
    
    def test_read_valid_numbers(self):
        """Test reading valid numbers from file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\n20\n5\n15\n")
            temp_file = f.name
        
        try:
            numbers = read_numbers_from_file(temp_file)
            assert numbers == [10.0, 20.0, 5.0, 15.0]
        finally:
            os.unlink(temp_file)
    
    def test_read_float_numbers(self):
        """Test reading float numbers from file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10.5\n20.7\n5.2\n")
            temp_file = f.name
        
        try:
            numbers = read_numbers_from_file(temp_file)
            assert numbers == [10.5, 20.7, 5.2]
        finally:
            os.unlink(temp_file)
    
    def test_read_negative_numbers(self):
        """Test reading negative numbers from file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("-10\n-5\n0\n5\n")
            temp_file = f.name
        
        try:
            numbers = read_numbers_from_file(temp_file)
            assert numbers == [-10.0, -5.0, 0.0, 5.0]
        finally:
            os.unlink(temp_file)
    
    def test_skip_empty_lines(self):
        """Test that empty lines are skipped."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\n\n20\n   \n30\n")
            temp_file = f.name
        
        try:
            numbers = read_numbers_from_file(temp_file)
            assert numbers == [10.0, 20.0, 30.0]
        finally:
            os.unlink(temp_file)
    
    def test_file_not_found(self):
        """Test FileNotFoundError for non-existent file."""
        with pytest.raises(FileNotFoundError):
            read_numbers_from_file("non_existent_file.txt")
    
    def test_invalid_number_format(self):
        """Test ValueError for invalid number format."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\nabc\n20\n")
            temp_file = f.name
        
        try:
            with pytest.raises(ValueError, match="Invalid number 'abc' on line 2"):
                read_numbers_from_file(temp_file)
        finally:
            os.unlink(temp_file)


class TestSortNumbers:
    """Test cases for sorting numbers."""
    
    def test_sort_unsorted_numbers(self):
        """Test sorting unsorted numbers."""
        numbers = [30, 10, 50, 20, 40]
        result = sort_numbers(numbers)
        assert result == [10, 20, 30, 40, 50]
    
    def test_sort_already_sorted(self):
        """Test sorting already sorted numbers."""
        numbers = [10, 20, 30, 40, 50]
        result = sort_numbers(numbers)
        assert result == [10, 20, 30, 40, 50]
    
    def test_sort_reverse_sorted(self):
        """Test sorting reverse-sorted numbers."""
        numbers = [50, 40, 30, 20, 10]
        result = sort_numbers(numbers)
        assert result == [10, 20, 30, 40, 50]
    
    def test_sort_with_duplicates(self):
        """Test sorting numbers with duplicates."""
        numbers = [30, 10, 30, 20, 10]
        result = sort_numbers(numbers)
        assert result == [10, 10, 20, 30, 30]
    
    def test_sort_negative_numbers(self):
        """Test sorting negative numbers."""
        numbers = [-5, -10, 0, 5, -2]
        result = sort_numbers(numbers)
        assert result == [-10, -5, -2, 0, 5]
    
    def test_sort_float_numbers(self):
        """Test sorting float numbers."""
        numbers = [3.5, 1.2, 4.8, 2.1]
        result = sort_numbers(numbers)
        assert result == [1.2, 2.1, 3.5, 4.8]
    
    def test_sort_empty_list(self):
        """Test sorting empty list."""
        numbers = []
        result = sort_numbers(numbers)
        assert result == []
    
    def test_sort_single_number(self):
        """Test sorting single number."""
        numbers = [42]
        result = sort_numbers(numbers)
        assert result == [42]


class TestWriteNumbersToFile:
    """Test cases for writing numbers to file."""
    
    def test_write_integers(self):
        """Test writing integer numbers to file."""
        numbers = [10.0, 20.0, 30.0]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            temp_file = f.name
        
        try:
            write_numbers_to_file(numbers, temp_file)
            
            with open(temp_file, 'r') as f:
                content = f.read()
            
            assert content == "10\n20\n30\n"
        finally:
            os.unlink(temp_file)
    
    def test_write_floats(self):
        """Test writing float numbers to file."""
        numbers = [10.5, 20.7, 30.2]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            temp_file = f.name
        
        try:
            write_numbers_to_file(numbers, temp_file)
            
            with open(temp_file, 'r') as f:
                content = f.read()
            
            assert content == "10.5\n20.7\n30.2\n"
        finally:
            os.unlink(temp_file)
    
    def test_write_mixed_numbers(self):
        """Test writing mixed integer and float numbers."""
        numbers = [10.0, 20.5, 30.0, 40.7]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            temp_file = f.name
        
        try:
            write_numbers_to_file(numbers, temp_file)
            
            with open(temp_file, 'r') as f:
                content = f.read()
            
            assert content == "10\n20.5\n30\n40.7\n"
        finally:
            os.unlink(temp_file)


class TestIntegration:
    """Integration tests for the complete workflow."""
    
    def test_complete_workflow(self):
        """Test the complete read-sort-write workflow."""
        # Create input file
        input_numbers = [50, 30, 80, 10, 60, 20, 90, 40, 70]
        expected_sorted = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            for num in input_numbers:
                f.write(f"{num}\n")
            input_file = f.name
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            output_file = f.name
        
        try:
            # Read, sort, and write
            numbers = read_numbers_from_file(input_file)
            sorted_numbers = sort_numbers(numbers)
            write_numbers_to_file(sorted_numbers, output_file)
            
            # Verify the result
            result_numbers = read_numbers_from_file(output_file)
            assert [int(n) for n in result_numbers] == expected_sorted
            
        finally:
            os.unlink(input_file)
            os.unlink(output_file)