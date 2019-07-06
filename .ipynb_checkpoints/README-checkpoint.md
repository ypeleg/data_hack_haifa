![alt text](imgs/logo.png)
<center><h1>Introduction to Data Science</h1></center>
<center><h5>Yam Peleg</h5></center>


-----


# Syllabus and Class Notes

<!--
A list to the notes from class can be found [here]().
-->
# Total time (including breaks): 3 Hours

Each section is about 45-55 minutes to allow for a small break between sections.
The tutorial will be a live-coding lecture, with a break for exercises and questions every 45-55 minutes.

## :00 - :45 Chapter 1: Pandas DataFrame Basics

- Running python
	- Anaconda, Python, IPython, and Jupyter notebooks
	- Installing packages
	- `conda` environments

Before we start cleaning data, let's begin by covering the basics of the Pandas library. We'll cover importing libraries in Python, and how to load your own datasets into Pandas. From there, you'll typically want to look around your data, so we'll cover various ways we can filter and look at our data, calculate simple aggregate statistics and visualize them. This section will end with how to save our data into files we can share with others.

- Loading your first dataset
- Looking at columns, rows, and cells
- Subsetting columns
- Subsetting rows
- Subsetting both columns and rows
- Boolean subsetting
- Grouped and aggregated calculations
- Export/save data



## :45 - 1:30 Chapter 2: Applying Functions

Sometimes we need a more complex method to tidy our data. Other times, we need to perform more complex tasks on our data. Here we'll cover how to write functions in Python and how to apply them to our data. This way, if a method does not exist to perform the task we want, or if we want to combine multiple tasks together, we can write our own custom functions to process our data.

- Writing a Python function
- Applying functions
- Vectorized functions

exercise: use the ebola dataset from the tidy section, and instead of using the .str. accessor, write a function to parse out the string.

## 1:30 - 2:15 Vizualizations with Seaborn

Getting ready for feature engineering

We visualise the data so we can do something with it.
This tutorial takes you through the basics and various functions of Seaborn. It is specifically useful for people working on data analysis. After completing this tutorial, you will find yourself at a moderate level of expertise from where you can take yourself to higher levels of expertise.

- Plotting
- Box plotting / Scatter Plotting
- Basic Statistics 

## 2:15 - 3:00 Feature Engineering

After we explored the data, it is time to work with it.
A common task is to fit some statistical model on our data.
One last processing task will be to convert our categorical variables into "dummy variables" for a model.
The goal of the last section is to how how pandas fits into the larger data science ecosystem.

- dummy variables
- linear regression in sklearn

exercise: fit a model on the titanic datset

<!-- #region -->



## Pre-readings

1. [A Quick Guide to Organizing Computational Biology Projects][1]
2. [Tidy Data][2]
3. [Best Practices for Scientific Computing][3]
4. [Good enough practices in scientific computing][4]

## Setup

### Python
<a href="https://www.anaconda.com/download/">Anaconda</a>,
an all-in-one installer, is recommended.

Regardless of how you choose to install it,
<strong>please make sure you install Python version 3.x</strong>
(e.g., 3.7 is fine).

When using the IPython notebook, a programming environment
that runs in a web browser, you will need a reasonably
up-to-date browser. The current versions of the Chrome, Safari and
Firefox browsers are all
<a href="http://ipython.org/ipython-doc/2/install/install.html#browser-compatibility">supported</a>
(some older browsers, including Internet Explorer version 9
and below, are not).

#### Windows
<a href="https://www.youtube.com/watch?v=xxQ0mzZ8UvA">Video Tutorial</a>
<ol>
<li>Open <a href="https://www.anaconda.com/download/">http://continuum.io/downloads</a> with your web browser.</li>
<li>Download the Python 3 installer for Windows.</li>
<li>Install Python 3 using all of the defaults for installation <em>except</em> make sure to check <strong>Make Anaconda the default Python</strong>.</li>
</ol>

#### Mac OS X
<a href="https://www.youtube.com/watch?v=TcSAln46u9U">Video Tutorial</a>
<ol>
<li>Open <a href="http://continuum.io/downloads">http://continuum.io/downloads</a> with your web browser.</li>
<li>Download the Python 3 installer for OS X.</li>
<li>Install Python 3 using all of the defaults for installation.</li>
</ol>

#### Linux
<ol>
<li>Open <a href="http://continuum.io/downloads">http://continuum.io/downloads</a> with your web browser.</li>
<li>Download the Python 3 installer for Linux.<br>
(Installation requires using the shell. If you aren't
comfortable doing the installation yourself
stop here and request help at the workshop.)
</li>
<li>
Open a terminal window.
</li>
<li>
Type <pre>bash Anaconda3-</pre> and then press
tab. The name of the file you just downloaded should
appear. If it does not, navigate to the folder where you
downloaded the file, for example with:
<pre>cd Downloads</pre>
Then, try again.
</li>
<li>
Press enter. You will follow the text-only prompts. To move through
the text, press the space key. Type <code>yes</code> and
press enter to approve the license. Press enter to approve the
default location for the files. Type <code>yes</code> and
press enter to prepend Anaconda to your <code>PATH</code>
(this makes the Anaconda distribution the default Python).
</li>
<li>
Close the terminal window.
</ol>

### Testing If Anaconda was installed
<!-- #endregion -->

1. Open up the Anaconda Command Prompt
2. Type "ipython" into the prompt
3. You should see Python open up with Python 3.7.x and using the Anaconda distribution
4. Type "quit()" to exit
5. Type "jupyer notebook" to launch the notebook (this may take a while if it is the first time you are launching it)
6. Note the URL (with the token), paste it into your browser
7. Close the anaconda prompt when you're done

[1]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424
[2]: http://vita.had.co.nz/papers/tidy-data.html
[3]: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745
[4]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510
