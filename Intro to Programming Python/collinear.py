from point import Point
import matplotlib.pyplot as plt

def read_points_from_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        points = []
        for i in range(n):
            x, y = map(float, f.readline().split())
            points.append(Point(x, y))
    return points

def get_slope(p1, p2):
    if p2.x == p1.x:
        return None
    return (p2.y - p1.y) / (p2.x - p1.x)

def are_collinear(p1, p2, p3, p4):
    slope1 = get_slope(p1, p2)
    slope2 = get_slope(p1, p3)
    slope3 = get_slope(p1, p4)
    if slope1 is None:
        return slope2 is None and slope3 is None
    return slope1 == slope2 and slope1 == slope3

def find_collinear_points(points):
    collinear_sets = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                for l in range(k+1, len(points)):
                    if are_collinear(points[i], points[j], points[k], points[l]):
                        collinear_sets.append((points[i], points[j], points[k], points[l]))
    return collinear_sets

def print_collinear_sets(collinear_sets):
    for s in collinear_sets:
        print(f"Line: ({s[0].x:}, {s[0].y:}), ({s[1].x:}, {s[1].y:}), ({s[2].x:}, {s[2].y:}), ({s[3].x:}, {s[3].y:})")

def plot_collinear_sets(points, collinear_sets):
    plt.scatter([p.x for p in points], [p.y for p in points], marker='.')
    for s in collinear_sets:
        plt.plot([s[i].x for i in range(4)], [s[i].y for i in range(4)], 'r')
    plt.show()

if __name__ == '__main__':
    filename = 'points1.txt'
    points = read_points_from_file(filename)
    collinear_sets = find_collinear_points(points)
    print_collinear_sets(collinear_sets)
    plot_collinear_sets(points, collinear_sets)
    filename = 'points2.txt'
    points = read_points_from_file(filename)
    collinear_sets = find_collinear_points(points)
    print_collinear_sets(collinear_sets)
    plot_collinear_sets(points, collinear_sets)
    filename = 'points3.txt'
    points = read_points_from_file(filename)
    collinear_sets = find_collinear_points(points)
    print_collinear_sets(collinear_sets)
    plot_collinear_sets(points, collinear_sets)
    filename = 'points4.txt'
    points = read_points_from_file(filename)
    collinear_sets = find_collinear_points(points)
    print_collinear_sets(collinear_sets)
    plot_collinear_sets(points, collinear_sets)
