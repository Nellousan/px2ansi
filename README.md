<br>
<p align="center">
<img width="360" height="144" src=".github/px2ansi.png">
</p>
<h3 align="center">Convert Pixel Art image to Text Art !</h3>
<p align="center"><i>
For all your needs to print fancy pixel art to your terminal.
</i></p>

# About

This tool convert pixel art image to text art using ANSI escape codes.
Motivated by the discovery of [arttime](https://github.com/poetaman/arttime), and the desire to use
my own custom pixel arts with it.
I've searched for a good converter but didn't find what i was looking for so this was an opportunity
to make my own.

<p align="center">
<img width="650" src=".github/demo.gif">
</p>

Compatible with any terminal supporting 24-bit ANSI Escape code and unicode characters.

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
Once you saved the output to a file, no need to use Px2ANSI anymore, you can simply print the content of
your file using `cat your_file.txt`, for example.\
<br>
More features to come.

# Roadmap

- [ ] Add a feature for default background color
- [ ] Add support for transparent pixel (between 0-255 alpha)

# License

Distributed under the GNU General Public License v3.0

# Contact

Twitter - [@Nellousan](https://twitter.com/Nellousan)\
Email - nellousan@hotmail.fr