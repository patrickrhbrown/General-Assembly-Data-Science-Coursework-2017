# Assignment: sampling

## Objectives

- Understanding the difference between a population and a sample
- Sampling from a population (`np.random.choice`)
- Computing mean, variance and standard deviation for a population and for a sample.

---- 

## Questions & Answers

1. Considering the population

  Imagine that we were able to survey an entire population. The resulting data is stored in `data/population.pkl`. With the `load_pickle` function in the [assignment\_2.py][1], we have access to these values as a numpy array.

	Go ahead and run the script in the command line (assumes you are in the code directory)
	```
	python assignment_2.py
	```
	and you will see 5 numbers printed out. These are the first 5 elements in the population list stored in `population`, a numpy array.

  Implement `get_mean`, as you did in the previous assignment, and implement `get_variance` for the argument `sample=False`. Don't worry about returning a value if `sample=True` for now. Do not use `np.mean` or `np.var`, we want you to write out the formula for this exercise.

_Done_

2. Sampling

  Usually it is simply unrealistic to survey an entire population. We use samples to gather information on the population.

  Implement `draw_sample` to draw a number of members randomly from the
  population. In the `if __name__ == '__main__'` block:

	  - Define a ```sample_100``` variable which draws 100 members.
	  - Define a ```sample_1000``` variable which draws 1000 members.

_Done_

3. Considering the samples

  Go back to the `get_variance` function, and make sure the right value is returned if `sample` is set to `True`.

_Done_

  Implement `get_sem` to calculate the standard error of the sample mean. The standard error of the mean measures how precisely we know the true mean of the population.

_Done_

4. Using the functions

  We are using the samples to estimate the mean and variance of the population.

  1. Print out the mean for the population (a parameter).
  2. Print out the mean for both samples (these are statistics).
  3. Print out the variance for the population and for both samples.

	- What is the percentage difference between variance of the sample
	of 1000 and variance of the sample of 100?

	YOUR ANSWER:

3. Define and calculate the variables `sem_100` and `sem_1000` by applying `get_sem` to the 100
sample and 1000 sample. Print the values.

_Done_

	- What is the percentage difference between SEM of the sample
	of 1000 and SEM of the sample of 100?
	
	YOUR ANSWER:  The percentage difference is -67% between the SEM of sample 1000 and SEM of sample 100 (or 67% expressed with the inputs inverted).
	
	- What information the SEM tells us that the variance does not?
	
	YOUR ANSWER:  The standard error of the mean represents the deviation of a sample mean from the population mean across samples drawn from that same population.  A small standard error is an indication that the sample mean is a (relatively) accurate reflection of the actual population mean.  As we have seen in this exercise, as the sample gets larger, the test statistic gets more accurate (the standard error gets smaller).  This is useful because when we conduct survey research, we often cannot draw data from the whole population; instead we have to construct samples via scientific processes in the hope of arriving at a fair reflection of the population.  Even so, it is not likely that the results of Sample B will be identical to Sample A, drawn from the same population.  If we were to draw an infinite number of samples of equal size from the population, we could display the observed means as a distribution.  We could then calculate a true population mean of all our sample means.  We could then also calculate the standard deviation of the distribution of sample means.  The Standard Deviation of this distribution of sample means is the Standard Error of each individual sample mean.  
	The variance represents the average variability of a set of scores, by taking the sum of squares divided by the number of values on which the set or sample is based.   The variance is also expressed in units that are not the same as the original data, and so can be more opaque in interpretation, which is why reversion to the standard error (and thus the original units) can aid analysis.  So the variance is helpful in giving a general idea of the spread of data within a sample or population, but SEM gives us insight as to the relationship between the sample mean and the population mean.

---- 
## Extra resources

- Khan Academy goes into the differences when computing the mean and variance for [population][2] vs for a [sample][3], and gives some intuition into the differences.

- a [cheatsheet][4] is available in the resources directory with compared/contrasted formulas for population vs sample mean and variance.

[1]:	../code/assignment_2.py
[2]:	https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/pop-variance-standard-deviation/v/range-variance-and-standard-deviation-as-measures-of-dispersion
[3]:	https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/sample-standard-deviation/v/sample-variance
[4]:	../resources/mean_variance.pdf