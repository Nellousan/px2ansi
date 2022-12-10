# Pixel Art to ANSI Escape code converter

<p align="center">Convert Pixel Art image to Text Art !</p>

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