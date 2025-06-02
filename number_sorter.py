#!/usr/bin/env python3
"""
Number Sorter - A program to sort numbers from a text file
"""

import sys
from typing import List


def read_numbers_from_file(filename: str) -> List[float]:
    """
    Read numbers from a text file.
    
    Args:
        filename: Path to the input file
        
    Returns:
        List of numbers as floats
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If file contains non-numeric values
    """
    numbers = []
    
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        number = float(line)
                        numbers.append(number)
                    except ValueError:
                        raise ValueError(f"Invalid number '{line}' on line {line_num}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    
    return numbers


def sort_numbers(numbers: List[float]) -> List[float]:
    """
    Sort a list of numbers in ascending order.
    
    Args:
        numbers: List of numbers to sort
        
    Returns:
        Sorted list of numbers
    """
    return sorted(numbers)


def write_numbers_to_file(numbers: List[float], filename: str) -> None:
    """
    Write numbers to a text file, one per line.
    
    Args:
        numbers: List of numbers to write
        filename: Output file path
    """
    with open(filename, 'w') as file:
        for number in numbers:
            # Format to remove unnecessary decimal places for integers
            if number.is_integer():
                file.write(f"{int(number)}\n")
            else:
                file.write(f"{number}\n")


def main():
    """Main function to handle command line arguments and execute sorting."""
    if len(sys.argv) != 3:
        print("Usage: python number_sorter.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Read numbers from input file
        print(f"Reading numbers from {input_file}...")
        numbers = read_numbers_from_file(input_file)
        print(f"Found {len(numbers)} numbers")
        
        # Sort the numbers
        print("Sorting numbers...")
        sorted_numbers = sort_numbers(numbers)
        
        # Write sorted numbers to output file
        print(f"Writing sorted numbers to {output_file}...")
        write_numbers_to_file(sorted_numbers, output_file)
        
        print("Sorting completed successfully!")
        print(f"Smallest number: {sorted_numbers[0]}")
        print(f"Largest number: {sorted_numbers[-1]}")
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
