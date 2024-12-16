from PIL import Image, ImageColor

# txt file constants
SMALL_MOUNTAIN = 'elevation_small.txt'
LARGE_MOUNTAIN = 'elevation_large.txt'


# Method and opens file and returns data inside


def open_file(file):
    with open(file, 'r') as f:
        entire_text = f.readlines()
        elevations_array = [x.split() for x in entire_text]

        # print(elevations_array)
        return elevations_array


# method to get dimension of final picture based off length of input
# small txt return 600,600 | large txt return 1201,1201
def get_dimensions(elevation_array):
    return len(elevation_array), len(elevation_array[0])


def get_min_and_max_elevation(elevation_array):
    temp = []
    for x in elevation_array:
        for y in x:
            temp.append(int(y))
    return (min(temp), max(temp))


# returns tuple of 3 integers representing the same color value i.e. (100,100,100)
def get_color_value(elevation, minimum, maximum):
    result = ((int(elevation) - int(minimum)) /
              (int(maximum) - int(minimum))) * 255

    return (int(result), int(result), int(result))


def create_picture(elevation_array):
    dimensions = get_dimensions(elevation_array)
    im = Image.new("RGBA", (dimensions))
    minimum = get_min_and_max_elevation(elevation_array)[0]
    maximum = get_min_and_max_elevation(elevation_array)[1]

    for x in range(dimensions[0]):
        for y in range(dimensions[0]):
            # ? no idea why y,x
            im.putpixel((y, x), get_color_value(
                elevation_array[x][y], minimum, maximum))

    im.save(str(dimensions[0]) + "_mountain.png")


def value_at_coordinates(elevation_array, current_coord):
    return int(elevation_array[current_coord[0]][current_coord[1]])


# create_picture(open_file(SMALL_MOUNTAIN))
# create_picture(open_file(LARGE_MOUNTAIN))


# method for testing logic


def f_around_method():
    pass
