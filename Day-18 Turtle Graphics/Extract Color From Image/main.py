# How to extract color from an Image.
import colorgram

rgb_colors = []
colors = colorgram.extract('hirst_painting_image.jpg', 56)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
