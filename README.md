# Pixel Art to ANSI Escape code converter




<p align="center">
<img width="360" height="144" src=".github/px2ansi.png">
Convert Pixel Art image to Text Art !
</p>

For all your needs to print fancy pixel art to your terminal.

![demo](.github/demo.gif)

Compatible with any terminal supporting 24-bit ANSI Escape code.

# How to use

Be sure to have the dependencies installed:
```
pip install -r requirements.txt
```

Basic usage:
```
python px2ansi.py your_image.png
```
This will print directly to the terminal, if you want to save it to a file you can use the `>`
redirection operator or use:
```
python px2ansi.py your_image.png -o your_file.txt
```

More features to come.

# Roadmap

[ ] Add a feature for default background color
[ ] Add support for transparent pixel (between 0-255 alpha)

# License

Distributed under the GNU General Public License v3.0