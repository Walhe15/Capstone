import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed) #mean
print(x)

# x = numpy.std(speed) #standard deviation
#x = numpy.mean(speed) #mean
# x = numpy.median(speed) #median
# x = numpy.var(speed) #variance
# x = numpy.percentile(age, 75) #percentile



# import numpy as np

# speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
# x = np.mean(speed)
# print(x)


#Normal Data Distribution

#To create data sets for testing we can use python module Numpy to create random data sets of any size.
# import numpy
# x = numpy.random.uniform(0.0, 5.0, 250) #this creates an array containing 250 random float between 0 and 5
# print(x)

#to plot graph using histogram
# import  matplotlib.pyplot as plt
# x = numpy.random.uniform(0.0, 5.0, 250)
#x = numpy.random.normal(5.0, 1.0, 100000) it can be normal distribution (line 29) or uniform (line 28).
# plt.hist(x, 5) In this case we are using histogram with 5 bars
# plt.show

#A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.
#We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.
#We specify that the mean value is 5.0, and the standard deviation is 1.0.



#Scatter Plot
#A scatter plot is a diagram where each value in the data set is represented by a dot.
#The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
# Use the scatter() method to draw a scatter plot diagram:
# import matplotlib.pyplot as plt
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# plt.scatter(x, y)
# plt.show()
# The x array represents the age of each car.
# The y array represents the speed of each car.
# What we can read from the diagram is that the two fastest cars were both 2 years old, and the slowest car was 12 years old.
# It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.

# Random Data Distributions. this is when we dont have the data to test for the algorithm, so we use random generated values
# import numpy
# import matplotlib.pyplot as plt
# x = numpy.random.normal(5.0, 1.0, 1000)
# y = numpy.random.normal(10.0, 2.0, 1000)
# plt.scatter(x, y)
# plt.show()


# Regression
# The term regression is used when you try to find the relationship between variables.
# In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

# Linear Regression
# Linear regression uses the relationship between the data-points to draw a straight line through all them.
# This line can be used to predict future values.

# this is the first step
# import matplotlib.pyplot as plt
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# plt.scatter(x, y)
# plt.show()

# this is the next step
# Import scipy and draw the line of Linear Regression:

# import matplotlib.pyplot as plt # line 82 and 83 means we import the module needed
# from scipy import stats
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# slope, intercept, r, p, std_err = stats.linregress(x, y). we execute this to return key values of linear regression
# def myfunc(x): #Create a function that uses the slope and intercept values to return a new value. This new value represents where on the y-axis the corresponding x value will be placed:
#   return slope * x + intercept
# mymodel = list(map(myfunc, x)) #Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
# plt.scatter(x, y) #Draw the original scatter plot:
# plt.plot(x, #mymodel) #Draw the line of linear regression:
# plt.show() #Display the diagram:

# R for Relationship
# It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, if there are no relationship the linear regression can not be used to predict anything.
# This relationship - the coefficient of correlation - is called r.
# The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.
# Python and the Scipy module will compute this value for you, all you have to do is feed it with the x and y values.

# How well does my data fit in a linear regression?

# from scipy import stats
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# slope, intercept, r, p, std_err = stats.linregress(x, y)
# print(r)

# The result -0.76 shows that there is a relationship, not perfect, but it indicates that we could use linear regression in future predictions.

# Predict Future Values
# Now we can use the information we have gathered to predict future values.
# Example: Let us try to predict the speed of a 10 years old car.
# To do so, we need the same myfunc() function from the example above:

# from scipy import stats
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# slope, intercept, r, p, std_err = stats.linregress(x, y)
# def myfunc(x): #this is the function that does the prediction
#   return slope * x + intercept
# speed = myfunc(10)
# print(speed)

# Idealy you should get a slanting slope for the graph , should you get a line that has no slope,
# the results are bad and there would not be any r relationship and this means you cant use the data for linear regression