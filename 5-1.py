import itertools
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class Segment:
    def __init__(self, a: Point, b: Point):
        self.A = a
        self.B = b

    def __str__(self):
        return f"[{self.A},{self.B}]"


def parse_segments(file):
    horizontal_segments = []
    vertical_segments = []

    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            a, b = line.split(' -> ')
            a_coords = list(map(int, a.split(',')))
            b_coords = list(map(int, b.split(',')))
            A = Point(a_coords[0], a_coords[1])
            B = Point(b_coords[0], b_coords[1])
            segment = Segment(A, B)

            if A.x == B.x:
                vertical_segments.append(segment)
            elif A.y == B.y:
                horizontal_segments.append(segment)

    return horizontal_segments, vertical_segments


def coordinate_range(segments: List[Segment], coordinate):
    coordinate_values = list(itertools.chain.from_iterable(
        list(map(lambda segment: [getattr(segment.A, coordinate), getattr(segment.B, coordinate)], segments))))
    return min(coordinate_values), max(coordinate_values)


if __name__ == '__main__':
    horizontal_segments, vertical_segments = parse_segments("vent_clouds.txt")
    # 327 lines in total, max point value should be 168

    horizontal_x_range = coordinate_range(horizontal_segments, 'x')
    vertical_x_range = coordinate_range(vertical_segments, 'x')

    horizontal_y_range = coordinate_range(horizontal_segments, 'y')
    vertical_y_range = coordinate_range(vertical_segments, 'y')

    complete_x_range = (horizontal_x_range[0] if horizontal_x_range[0] < vertical_x_range[0] else vertical_x_range[0],
                        horizontal_x_range[1] if horizontal_x_range[1] > vertical_x_range[1] else vertical_x_range[1])

    complete_y_range = (horizontal_y_range[0] if horizontal_y_range[0] < vertical_y_range[0] else vertical_y_range[0],
                        horizontal_y_range[1] if horizontal_y_range[1] > vertical_y_range[1] else vertical_y_range[1])

    grid = [[0] * (complete_x_range[1] - complete_x_range[0] + 1) for _ in
            range(complete_y_range[1] - complete_y_range[0] + 1)]

    for horizontal_segment in horizontal_segments:
        x_range = range(horizontal_segment.A.x - complete_x_range[0], horizontal_segment.B.x - complete_x_range[
            0] + 1) if horizontal_segment.A.x < horizontal_segment.B.x else range(
            horizontal_segment.B.x - complete_x_range[0], horizontal_segment.A.x - complete_x_range[0] + 1)

        for x in x_range:
            grid[horizontal_segment.A.y - complete_y_range[0]][x] += 1

    for vertical_segment in vertical_segments:
        y_range = range(vertical_segment.A.y - complete_y_range[0],
                        vertical_segment.B.y - complete_y_range[
                            0] + 1) if vertical_segment.A.y < vertical_segment.B.y else range(
            vertical_segment.B.y - complete_y_range[0], vertical_segment.A.y - complete_y_range[0] + 1)

        for y in y_range:
            grid[y][vertical_segment.A.x - complete_x_range[0]] += 1

    flat_grid = list(itertools.chain.from_iterable(grid))
    print(len(list(filter(lambda value: value > 1, flat_grid))))
