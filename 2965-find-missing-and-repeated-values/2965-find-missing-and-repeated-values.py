class Solution:
    def findMissingAndRepeatedValues(self, grid):
        
        n = len(grid)

        total_numbers = n * n

        expected_sum = total_numbers * (total_numbers + 1) // 2

        expected_square_sum = (
            total_numbers * (total_numbers + 1) * (2 * total_numbers + 1)
        ) // 6

        actual_sum = 0
        actual_square_sum = 0

        # Traverse 2D grid
        for row in grid:
            for num in row:
                actual_sum += num
                actual_square_sum += num * num

        diff = actual_sum - expected_sum

        square_diff = actual_square_sum - expected_square_sum

        sum_xy = square_diff // diff

        repeating = (diff + sum_xy) // 2

        missing = repeating - diff

        return [repeating, missing]