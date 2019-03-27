# color-shifter
dual tone, categorical based color converter for pictures

### inputs
- image file name (png/jpg/mainstream types)
- number of categories (size of color gradient)
- dark color (hex)
- light color (hex)

### additional modifications
- if you are so inclined you can manually adjust categories to have a specific color (I like making the 0/lowest category a dark color for a cool effect as shown below)

### usage requirements
- python3
- PIL
`pip3 install Pillow`
- numpy
`pip3 install numpy`

### known bugs
- certain categorial values error (16) due to hacky math

# demo

### before
![profile](./profile.jpg)

### after
![profile](./profile-shifted.jpg)
