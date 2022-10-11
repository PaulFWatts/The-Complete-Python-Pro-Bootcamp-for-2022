import colorgram

rgb_colors = []
colors = colorgram.extract(
    "./Day 018 Understanding Turtle Graphics/hirst_painting/image.jpeg",
    30,
)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


print(rgb_colors)

# Copy the printed colours and remove the colours that are close to white
# Then copy color_list into list_comprehension.py
color_list = [
    (139, 164, 183),
    (21, 118, 177),
    (240, 213, 59),
    (204, 139, 166),
    (223, 158, 84),
    (122, 72, 98),
    (142, 20, 36),
    (20, 138, 58),
    (190, 175, 23),
    (71, 30, 36),
    (195, 72, 33),
    (225, 171, 198),
    (57, 35, 32),
    (25, 170, 184),
    (236, 85, 33),
    (7, 111, 66),
    (109, 190, 136),
    (42, 173, 81),
    (183, 94, 110),
    (188, 183, 210),
    (39, 38, 45),
    (156, 208, 216),
    (154, 213, 175),
    (241, 171, 151),
    (229, 212, 16),
    (125, 115, 160),
]
