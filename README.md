# from-the-ground-up

Teaching material for Brightway2.5, starting from the foundations. A different approach from the existing teaching material which describes *how* Brightway works, with a focus on *why* Brightway does what it does.

## Installation

There are a number of ways to install Brightway 2.5; `pip` works well, except that the fast linear algebra libraries are not available for MacOS, so we use `anaconda`, which works for all major OSes. Please follow these instructions exactly, it is easy to make small changes which will have undesired effects later on.

0. Create a new directory store data and scripts in a location that will be easy for you to find and type, like your desktop.

1. Install miniconda: https://docs.conda.io/en/latest/miniconda.html. If you already have anaconda, you can also use that.

2. Open a terminal program. On Windows, this is the Anaconda shell (not the Powershell one, unless you are more comfortable in the Powershell).

3. Paste and execute the following command into your terminal:

    conda create -n bw25

This will create [a virtual environment](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/), a safe place to install Brightway that won't interact with other Python installations or environments.

4. Activate this environment, following the instructions you were given. You will need to type and execute something like `conda activate bw25`. Afterwards, you will probably see something like `(bw25)` as part of your your terminal line. If you see `(base)`, you haven't activated the bw25 environment!

5. Install Brightway by pasting the following:

    conda install -c conda-forge -c defaults -c cmutel jupyterlab brightway25

6. After installation, you can check to make sure you have the correct versions in an iPython shell:

Type `ipython` to enter the shell. Then run:

    import bw2data; bw2data.__version__

You should get `(4, 0, 'DEVX')`, where X is a number higher than 5.

## Using the notebooks

You can download (and then unzip) this repository, or use `git` to clone it; in either case, put it somewhere you can easily get to from the terminal. Than use `cd` to get to this directory. For example, on my machine I downloaded the repo to my `Downloads` folder, so I would run `cd Downloads/from-the-ground-up`. Often you can use `<tab>` to autocomplete long file names to save a bit of time.

Once you are in the directory, with the `bw25` environment active, you can run `jupyter-lab`, and go through the notebooks in numerical order.

## Basic Python knowledge

In order for these notebooks to be an enjoyable and productive experience, you will need to have mastered the basics of programming in Python. NO need to be an expert, but you should at least know the following:

* What is a variable, and how to define, use, and change its value
* What are lists, tuples, sets, and dicts
* List comprehensions
* How to define and use functions, including the use of `*args` and `**kwargs`

In addition, you should read (and play with the executable notebooks) in [the Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html). If you have time, I also recommend reading the chapters from that book on Pandas and Matplotlib.
