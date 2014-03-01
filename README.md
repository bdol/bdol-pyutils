This is a large Python file containing a lot of the functions that I reuse when
writing Python ML code. While it's not the cleanest solution, I have one large
file to make dependencies a bit easier to manage.

Included are the following:

- progBar  
 - Prints a progress bar to stdout (inspired by this SO post: http://stackoverflow.com/questions/3002085/python-to-print-out-status-bar-and-percentage). Give it the current step (t) and the toal number of steps (N), and it will print a continuously updating progress bar.

- loadMNIST
 - Loads the MNIST dataset from the widely-available pickled version of the dataset (http://deeplearning.net/data/mnist/mnist.pkl.gz). Note that this takes a path to the unzipped file. Allows you to specify which digits to use, and whether or not to use a bit vector for labels (a vector of with a 1 corresponding to the label of the current sample, and zeros elsewhere).
