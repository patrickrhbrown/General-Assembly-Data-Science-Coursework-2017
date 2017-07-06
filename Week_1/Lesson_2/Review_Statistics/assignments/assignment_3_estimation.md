# Assignment: Estimation

## Objectives
This is first glimpse into inference.

- computing confidence intervals for population proportions
- computing confidence intervals for population means
- choosing the appropriate test statistics

---- 

## Questions & Answers

A   confidence  interval    (CI)    is  an  interval    estimate    of  a   population  parameter.

### 1. Estimating population proportion

Let us consider polling. We want to survey a population size of N=12000. We randomly select people to survey to form a sample n=300 members strong and submit a yes(1)/no(0) question. p=140 people answered positively.

  - What is the sample mean? Its variance?

  YOUR ANSWER: 0.46 or 46% 

  YOUR EXPLANATION: We want to identify the mean positive response rate within the sample.  As such we take how many people responded in the affirmative to the question and divide that by the number in the sample to obtain our sample mean.  

I want to estimate the proportion of people who answered positively, what is the point estimate? the margin of error for a 95% confidence interval? (Justify your choice of test statistics.)

  YOUR ANSWER: Ran out of time.  Will revisit.

  YOUR EXPLANATION:

### 2. Estimating a population mean

In [assignment\_3.py][1], notice how the functions `load_pickle`, `draw_sample`, `get_mean` and `get_sem` from your completed version of [assignment\_2.py][2] were imported. You will use them in this part of the assignment.

  ```python
  from assignment_2 import load_pickle, draw_sample, get_mean, get_sem
  ```

1. Implement `get_confidence_interval` to calculate the confidence intervals of the 100 sample and 1000 sample using confidence of `.95`.
  Use `scs.t.ppf(percentile)` to get a value at a given percentile in a t-distribution

2. Define the variables `ci_100` and `ci_1000` and apply the function.
Print the variables.

	- Does the confidence intervals include the population mean? Can you explain
	why that is?
	
	YOUR ANSWER: For the sample of 100, the confidence interval does include the population mean.  For the sample of 1000 it does not.
	
	YOUR EXPLANATION: we repeatedly drew samples of the same size from a population and constructed 95% confidence intervals for each sample of 100 and 1000, and we repeated this process 1000 times. Then we would expect 95%, or 95 or 950, of these confidence intervals to contain the true population parameter. In reality, though, we typically construct only one such confidence interval and thus we are X-% confident that this interval has captured the true parameter. However in reality, this interval might or might not contain the true value. As a result, confidence intervals are exactly that: statements of how *confident* you are. These should not be interpreted, for example, to say that there is a 95% probability that the true value is in this interval. This is not true because the true value is either in the interval (i.e. probability of 1) or not in the interval (probability of 0).

3. Modifying function arguments:
	- Try lowering the confidence to `.70` instead of `.95`. What does it do to the range of the confidence interval?

	YOUR ANSWER: the range narrows within which we consider the population mean to lie.

	YOUR EXPLANATION: Ultimately, by decreasing the confidence level, we are decreasing our level of confidence that our interval contains the mean.

4. Assumptions: What assumption are we making about the distribution of the population when we apply the confidence interval? Why are we able to make this assumption here without visualizing any plot?

	YOUR ANSWER: we are assuming that as the sampling distribution of the sample mean gets larger, it tends toward normal.

	YOUR EXPLANATION: The central limit theorem tells us exactly what the shape of the distribution of means will be when we draw repeated samples from a given population.  Specifically, as the sample sizes get larger, the distribution of means calculated from repeated sampling will approach normality.  It is easy to show that the mean of this sampling distribution will be the population mean, and that the variance will be equal to the population variance divided by n.  If we take the square root of the variance, we get the standard deviation of the sampling distribution, which we call the standard error.  This information together tells us that the mean of the sample means will be equal to the population means, and the variance will get smaller when 1) the population variance gets smaller, or 2) the sample sizes get larger.

	This result holds no matter what shape the original sample distribution may have been.

---- 
## Extra resources

- Khan Academy explains how to build confidence intervals to give an interval estimate of a population parameter (https://www.khanacademy.org/math/statistics-probability/confidence-intervals-one-sample).

- JBStatistics material: these are videos that introduce you to the notion and the building of confidence intervals (http://www.jbstatistics.com/confidence-intervals/)

- a [cheatsheet][3] is available in the resources directory with compared/contrasted formulas for confidence intervals depending on whether the population standard deviation is known or not.

[1]:	../code/assignment_3.py
[2]:	../code/assignment_2.py
[3]:	../resources/CI.pdf