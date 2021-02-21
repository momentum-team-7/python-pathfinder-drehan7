import random
from PIL import Image

from pathfinder import open_file, get_min_and_max_elevation

mountain_image = Image.open('600_mountain.png')

elevation_array = open_file('elevation_small.txt')


def get_elevation(elevation_array, coord):
    return int(elevation_array[coord[0]][coord[1]])


def draw_lines(image, path_list):
    for list_path in path_list:
        for path in list_path:
            image.putpixel((path[0], path[1]), (255, 0, 0))

    image.save('all_paths_drawn.png')
    return image


def draw_best_line(image, path):
    for coord in path:
        image.putpixel((coord[0], coord[1]), (0, 255, 0))

    image.save("best_path.png")

# return list of coordinates to draw in later


def get_path(elevation_array, y_coord):
    # initialize list with starting coordinate
    starting_coord = (0, y_coord)
    path_list = [starting_coord]

    # while x coordinate is not at the end of picture
    while starting_coord[0] < len(elevation_array) - 1:
        if starting_coord[1] == 0:
            starting_coord = handle_top(elevation_array, starting_coord)
            path_list.append(starting_coord)
        elif starting_coord[1] == len(elevation_array) - 1:
            starting_coord = handle_bottom(elevation_array, starting_coord)
            path_list.append(starting_coord)
        else:
            starting_coord = get_next_coord(elevation_array, starting_coord)
            path_list.append(starting_coord)

    return path_list


def get_best_path():
    all_left_coords = []
    for line in elevation_array:
        all_left_coords.append(int(line[0]))
    # print(str(min(all_left_coords)) + " y-value is " +
    #       str(all_left_coords.index(min(all_left_coords))))
    min_start_coord = (0, all_left_coords.index(min(all_left_coords)))
    return get_path(elevation_array, min_start_coord[1])


def get_all_paths():
    all_paths = []
    for x in range(len(elevation_array) - 1):
        all_paths.append(get_path(elevation_array, x))
    # for path in all_paths:
    #     print(path)
    return all_paths


def get_next_coord(elevation_array, starting_coord):
    straight_coord = (starting_coord[0] + 1, starting_coord[1])
    left_coord = (starting_coord[0] + 1, starting_coord[1] - 1)
    right_coord = (starting_coord[0] + 1, starting_coord[1] + 1)

    current_elevation = get_elevation(elevation_array, starting_coord)
    left_elevation = get_elevation(elevation_array, left_coord)
    right_elevation = get_elevation(elevation_array, right_coord)
    straight_elevation = get_elevation(elevation_array, straight_coord)

    left_diff = abs(current_elevation - left_elevation)
    straight_diff = abs(current_elevation - straight_elevation)
    right_diff = abs(current_elevation - right_elevation)

    if left_diff < straight_diff and left_diff < right_diff:
        return left_coord
    elif right_diff < left_diff and right_diff < straight_diff:
        return right_coord
    elif right_diff == left_diff and right_diff < straight_diff:
        temp = (left_coord, right_coord)
        return temp[random.randint(0, 1)]
    else:
        return straight_coord


# handle if path hits very top of map
def handle_top(elevation_array, starting_coord):
    straight_coord = (starting_coord[0] + 1, starting_coord[1])
    right_coord = (starting_coord[0] + 1, starting_coord[1]+1)

    straight_elevation = get_elevation(elevation_array, straight_coord)
    right_elevation = get_elevation(elevation_array, right_coord)
    current_elevation = get_elevation(elevation_array, starting_coord)

    straight_diff = abs(current_elevation - straight_elevation)
    right_diff = abs(current_elevation - right_elevation)

    if right_diff < straight_diff:
        return right_coord
    else:
        return straight_coord


# handle if path hits bottom of map
def handle_bottom(elevation_array, starting_coord):
    straight_coord = (starting_coord[0] + 1, starting_coord[1])
    left_coord = (starting_coord[0] + 1, starting_coord[1] - 1)

    straight_elevation = get_elevation(elevation_array, straight_coord)
    left_elevation = get_elevation(elevation_array, left_coord)
    current_elevation = get_elevation(elevation_array, starting_coord)

    straight_diff = abs(current_elevation - straight_elevation)
    left_diff = abs(current_elevation - left_elevation)

    if left_diff < straight_diff:
        return left_coord
    else:
        return straight_coord


def run():
    paths = get_all_paths()
    draw_best_line(draw_lines(mountain_image, paths), get_best_path())
    print('done')


run()
# get_best_path()
