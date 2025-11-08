import pytest

from heap_sort import heap_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort


test_cases = [
    # (input, expected, description)
    ([], [], "Empty array"),
    ([1], [1], "An array of one element"),
    ([1, 1, 1, 1], [1, 1, 1, 1], "All the elements are the same"),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "Back sorted array"),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "An already sorted array"),
    ([3, 2], [2, 3], "An array of two elements"),
    ([-1, -3, 2, 0, -5], [-5, -3, -1, 0, 2], "With negative numbers"),
    ([1, 2, 3, 2, 1], [1, 1, 2, 2, 3], "With repeating elements"),
    ([float('inf'), 1, float('-inf')], [float('-inf'), 1, float('inf')],
    "With infinities"),
    ([3.14, 1.41, 2.71], [1.41, 2.71, 3.14], "fractional numbers"),
]

@pytest.mark.parametrize("input_arr,expected,description", test_cases)
def test_quick_sort(input_arr, expected, description):
    result = quick_sort(input_arr.copy())
    assert result == expected, f"QuickSort failed: {description}"

@pytest.mark.parametrize("input_arr,expected,description", test_cases)
def test_bubble_sort(input_arr, expected, description):
    result = bubble_sort(input_arr.copy())
    assert result == expected, f"BubbleSort failed: {description}"

@pytest.mark.parametrize("input_arr,expected,description", test_cases)
def test_merge_sort(input_arr, expected, description):
    result = merge_sort(input_arr.copy())
    assert result == expected, f"MergeSort failed: {description}"

@pytest.mark.parametrize("input_arr,expected,description", test_cases)
def test_heap_sort(input_arr, expected, description):
    result = heap_sort(input_arr.copy())
    assert result == expected, f"HeapSort failed: {description}"
