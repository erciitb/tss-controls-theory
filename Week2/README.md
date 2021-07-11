# Line Follower

The filed python files contain starter environments in which you have to add your own code.

Your task is to add a PID controller to control the movement of the car/robot and make it follow the drawn path.

## Get Started

### Installing Python and VSCode

In case you do not have python, and a text editor installed then, we would recommend that you check out [this video](https://youtu.be/dNFgRUD2w68) so that you have a nice setup to work with for the rest of the week!

### Downloading and Running the code

Download the repo as a zip file by clicking on [this link](https://github.com/erciitb/tss-controls-theory/archive/refs/heads/main.zip) and expand it in a convenient location.

Now open a terminal inside the directory week 2 within the expanded folder. Then type the following commands to run the code.

```bash
pip install pygame
python line_follower_dist.py # for the dist method
python line_follower_color.py # for the color sensor method
```

## Resources

### PID Tuning

Refer to the last few sections of the week 1([click here](https://colab.research.google.com/drive/1uOsE_tVoBd8ANP4vq-xk6BhoZzq9OQC9#scrollTo=519f0c10)) material for this topic, especially the python code at the end.

### PID refresher

You can go through this [PID Playlist](https://youtube.com/playlist?list=PLn8PRpmsu08pQBgjxYFXSsODEF3Jqmm-y) for a quick refresher on what PID control is and how it is used.
You don't need to watch the whole playlist, this is just to refresh a few key concepts that will be used.

### Python and pygame resources(optional)

- [pygame documentation](https://www.pygame.org/docs/) - Very useful for finding useful functions, specially [this - pygame.math.Vector2](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2)
- [Pygame tutorial](https://youtu.be/FfWpgLFMI7w) - do only what is required
- [Python tutorial](https://youtu.be/_uQrJ0TkZlc) - Feel free to skip sections since we have already covered the same concepts in CS101

## Methods

Two methods of solving this problem are listed below. You can use one of them or possibly even come up with your own method to tackle this problem.

Some extra details for each method are given in the comments in the respective files.

### Color Sensor Method

In this method a few, say 3(try and see if more or less work better), sensors are placed in front of the car. Each of the sensors collects data about the color below(pygame has this functionality) and based on that the car is made to turn right or left.
Watch this video for reference: [video](https://www.youtube.com/watch?v=bL0MmeQhpAQ)

The starter code for this type is in the file `line_follower_color.py`.

### Distance Method

This method makes use of sensors to find the distance of the car from a certain reference and then the controller decides how much to turn and which direction.
Watch this video for an explanation of how a more advanced type this method works: [video](https://youtu.be/4Y7zG48uHRo)

The starter code for this type is in the file `line_follower_dist.py`

The file itself contains more info about the code and implementation in the form of comments.

## Attribution

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
