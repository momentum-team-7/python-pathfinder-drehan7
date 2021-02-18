from PIL import Image, ImageColor

# txt file constants
SMALL_MOUNTAIN = 'elevation_small.txt'
LARGE_MOUNTAIN = 'elevation_large.txt'


# Method and opens file and returns data inside
def open_file(file):
    with open(file, 'r') as f:
        entire_text = f.readlines()
        return entire_text


# method to get dimension of final picture based off length of input
# small txt return 600,600 | large txt return 1201,1201
def get_dimensions(file_contents):
    entire_text = file_contents
    return len(entire_text), len(entire_text[0].split())


def get_min_elevation(file_contents):
    return min(min(file_contents).split())


def get_max_elevation(file_contents):
    return max(max(file_contents).split())


# returns tuple of 3 integers representing the same color value i.e. (100,100,100)
def get_color_value(elevation, minimum, maximum):
    result = ((int(elevation) - int(minimum)) /
              (int(maximum) - int(minimum))) * 255

    return (int(result), int(result), int(result))


def create_picture():
    file_contents = open_file(LARGE_MOUNTAIN)
    dimensions = get_dimensions(file_contents)
    im = Image.new("RGBA", (dimensions))
    minimum = get_min_elevation(file_contents)
    maximum = get_max_elevation(file_contents)
    elevation = 20000

    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            im.putpixel((x, y), get_color_value(
                file_contents[x].split()[y], minimum, maximum))

    im.save('testPixels.png')

    print(im.getpixel((0, 0)))
    print("the second value of the text file (should be 4710) ",
          file_contents[0].split()[1])


# method for testing logic
def f_around_method(color_value):
    im = Image.new("RGBA", (100, 100))

    print(im.getpixel((0, 0)))

    for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (color_value, color_value, color_value))

    for x in range(100):
        for y in range(50, 100):
            im.putpixel((x, y), (100, 100, 100))


create_picture()
