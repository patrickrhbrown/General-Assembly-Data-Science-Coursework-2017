# Assignment: Summary metrics

## Objectives

We want to describe a dataset thanks to some key summary metrics. We will be

  - implementing mean, median and mode as well as when to use each summary metric
  - investigating range, interquartile range and outliers

Remember that plotting out data is still the best way to understand it. Checkout [Anscombe's quartet][1].

---- 

## Questions & Answers

Brief recap: notice the `if __name__ == '__main__':` block in the `.py` file. The code in this block will run when you type in the command prompt `python assignment_1_summary_stats.py`. Here it is mostly a check for our functions.

1. Mean, median, mode

  (a) Fill in the functions `get_mean`, `get_median`, and `get_mode` in [assignment\_1.py][2]. For the sake of practice, do not use `np.mean`, `np.median` and `scs.mode`.

  (b) Brief dataset description
	- dataset_1 : prices from used cars in my price range.
	- dataset_2 : prices of used cars I can afford and my dream car, a brand new Audi A8L.
	- dataset_3 : prices from used and new cars on Craiglist.

  Which summary metric would you choose to best describe datasets 1 to 3?

  YOUR ANSWER:
	Dataset_1: in this case, the mean would be a helpful statistic with a view to understanding the 'typical' car price within the price range. 
	Dataset_2: the mean would not be appropriate in this case. If the Audi 8L is signficantly higher in value than the affordable cars in the price range, it would drag the mean of the rest of lower values towards it and give an overall misleading impression of the average price.  The median would give an appreciation of the car price in the middle of the range, and would serve to lluminate that difference between 'sensible' and 'dream car'.
	Dataset_3: given that on Craigslist, it would be helpful to have an idea of the range of values within the price range, the mode would be a suitable choice since it would flag the frequency of values across car types if organised by price.  The mode would help to avoid some of the distortions that come from a) mixed old and new cars and b) the possible 'error' that accompanies the seller-sets-the-price model of peer to peer selling, and most importantly help to make sense of it.
 YOUR EXPLANATION:

Dataset\_1 

2. Range vs interquartile range
  Fill in the functions `get_range`, `get_IQR`, and `remove_outliers` in [assignment\_1.py][3]. Look up how to use `np.percentile`.

How are range and interquartile range similar? How are they different?

  YOUR ANSWER: _The range and the interquartile range are both ways to obtain an idea of a dataset's spread or dispersion, permitting us to see how much the data varies.  Interquartile range offers us a means to get a stronger take on the structure of the data, since it affords us an initial estimate of outliers by quickly assessing whether values lie 1.5 times IQR below or above the first and third quartile respectively.  Comparing the IQR to the median, we can also detect skewness in the data (a higher proportion of lower or higher values)._
  
_The range tells us in general how well the central tendency represents the data.  A large range suggests the central tendency is not as representative of the data as it would be if the range was small.  As the range measures the difference between the largest and smallest values in a dataset, it is more sensitive to outliers in the data than the IQR._

_If there are outliers in your dataset, how do you decide if you are going to ignore them or keep them in your analysis?_

  YOUR ANSWER: _For modest-size datasets, conventional approaches to exclusion are that outliers that are beyond around 1.5 times IQR or more above or below the IQR should be at least probed further.  The question as to what to do with them really depends on the context at hand. If you are seeking an underserved market in an already-dominated market place and you discover a series of customers that are not currently being serviced by an offering that fits them, these outliers might be a serendipitous find.  A first step should be to determine if such outliers represent erroneous or highly improbable data using judgement and reasoning, and such values can arguably be removed.  However, if values are being removed to simply fit a model, this runs the risk of overfitting._

_In 'big' data sets, adjusting for an optimal approach toward variance vs bias becomes a parameter simply to be managed.  Again, judgement comes into play.  Certainly, in a technique such as linear regression, which seeks to minimise the residual sum of squares, outliers will skew results.  Yet their exclusion, if entirely valid data, could present a misleading impression of the validity/reliability of the model._

_In both circumstances, the mantra of reproducibility and scientific method dictates that we should record how and why any outliers are excluded from consideration._
  

---- 
## Extra resources

- These are relatively basic notions, they are defined in Khan Academy (https://www.khanacademy.org/math/statistics-probability/displaying-describing-data) and Udacity (https://classroom.udacity.com/courses/st101/) courses.

[1]:	https://en.wikipedia.org/wiki/Anscombe's_quartet
[2]:	../code/assignment_1.py
[3]:	../code/assignment_1.py