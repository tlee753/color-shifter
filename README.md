# color-shifter
dual tone, categorical based color converter for pictures

### inputs
- image file name (png/jpg/mainstream types)
- number of categories (size of color gradient)
- dark color (hex)
- light color (hex)

### usage requirements
- python3
- PIL
`pip3 install Pillow`
- numpy
`pip3 install numpy`

### known bugs
- certain categorial values error (16) due to hacky math

### before
![profile](./profile.jpg)

### after
![profile](./profile-shifted.jpg)
