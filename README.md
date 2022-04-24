# from-the-ground-up

Teaching material for Brightway2.5, starting from the foundations. A different approach from the existing teaching material which describes *how* Bightway works, with a focus on *why* Brightway does what it does. These notebooks are designed to be used in class, so do not contain a ton of instruction.

## Installation

Brightway can be installed via `pip` or `conda`; we give instructions here for `conda`. Please follow these instructions exactly.

0. Download or move these files to a location that will be easy for you to find and type, like your desktop.

1. Install miniconda: https://docs.conda.io/en/latest/miniconda.html. If you already have anaconda, you can also use that.

2. Open a terminal program. On Windows, this is the Anaconda shell (not the Powershell one, unless you are more comfortable in the Powershell).

3. Paste and execute the following command into your terminal:

    conda create -n bw25 -c conda-forge -c defaults -c cmutel brightway25 jupyterlab

This will create [a virtual environment](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/), a safe place to install Brightway that won't interact with other Python installations or environments. You can change the name `bw25` if that is already used.

4. Activate this environment by typing `conda activate bw25`. Afterwards, you will probably see something like `(bw25)` as part of your your terminal prompt. If you see `(base)`, you haven't activated the bw25 environment!

5. After installation, you can check to make sure you have the correct versions in an iPython shell:

Type `ipython` to enter the shell. Then run:

    import bw2data; bw2data.__version__

You should get `(4, 0, 'DEVX')`, where X is a number higher than 12.

## Restarting the next day

1. Open a terminal window ( on Windows, `Anaconda Prompt (miniconda3)`)

2. Change to your notebook directory using cd, e.g. `cd Downloads/from-the-ground-up-main/`

3. Activate your environment, e.g. `conda activate bw25`

4. Run `jupyter-lab`

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
