# Assignment: Summary metrics

## Objectives

We want to describe a dataset thanks to some key summary metrics. We will be

  - implementing mean, median and mode as well as when to use each summary metric
  - investigating range, interquartile range and outliers

Remember that plotting out data is still the best way to understand it. Checkout [Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe's_quartet).

_______________________________________

## Questions & Answers

Brief recap: notice the `if __name__ == '__main__':` block in the `.py` file. The code in this block will run when you type in the command prompt `python assignment_1_summary_stats.py`. Here it is mostly a check for our functions.

1. Mean, median, mode

  (a) Fill in the functions `get_mean`, `get_median`, and `get_mode` in [assignment_1.py](../code/assignment_1.py). For the sake of practice, do not use `np.mean`, `np.median` and `scs.mode`.

  (b) Brief dataset description
    - dataset_1 : prices from used cars in my price range.
    - dataset_2 : prices of used cars I can afford and my dream car, a brand new Audi A8L.
    - dataset_3 : prices from used and new cars on Craiglist.

  Which summary metric would you choose to best describe datasets 1 to 3?

  YOUR ANSWER:
  
  1 Dataset_1: using the mean would help 
  	Dataset_2: the mean would not be appropriate in this case if the Audi 8L is signficantly higher in value than the affordable cars in the price range since it would drag the mean of the rest of lower values towards it.  The median in this case would be more appropriate since 
  	Dataset_3: Mode or median
   
 YOUR EXPLANATION:

Dataset_1 

2. Range vs interquartile range
  Fill in the functions `get_range`, `get_IQR`, and `remove_outliers` in [assignment_1.py](../code/assignment_1.py). Look up how to use `np.percentile`.

How are range and interquartile range similar? How are they different?

  YOUR ANSWER: _The range and the interquartile range are both ways to obtain an idea of a dataset's spread or dispersion, pemitting us to see how much the data varies.  Interquartile range offers us a means to get a stronger take on the structure of the data, since it affords us an initial estimate of outliers by quickly assessing whether values lie 1.5 times IQR below or above the first and third quartile respectively.  Comparing the IQR to the median, we can also detect skewness in the data (a higher proportion of lower or higher values).
  
  The range tells us in general how well the central tendency represents the data.  A large range suggests the central tendency is not as representative of the data as it would be if the range was small.  As the range measures the difference between the largest and smallest values in a dataset, it is more sensitive to outliers in the data than the IQR.

If there are outliers in your dataset, how do you decide if you are going to ignore them or keep them in your analysis?

  YOUR ANSWER: _For modest datasets, conventional approaches to exclusion are that outliers that are beyond around 1.5 times IQR or more above or below the IQR should be at least probed further.  The question as to what to do with them really depends on the context at hand. If you are seeking an underserved market in an already dominated market place and you discover a series of customers that are not currently being serviced by an offering that fits them, these outliers might be a serendipitous find.  A first step should be to determine if such outliers represent erroneous or highly improbable data using judgement and reasoning, and such values can arguably be removed.  However, if values are being removed to simply fit a model, this runs the risk of overfitting.

In 'big' data sets, adjusting for an optimal approach toward variance vs bias becomes a parameter simply to be managed.  Again, judgement comes into play.  Certainly, in a technique such as linear regression, which seeks to minimise the residual sum of squares, outliers will skew results.  Yet their exclusion, if entirely valid data, could present a misleading impression of the validity/reliability of the model.

In both circumstances, the mantra of reproducibility and scientific method dictates that we should record how and why any outliers are excluded from consideration.
  

_______________________________________
## Extra resources

- These are relatively basic notions, they are defined in Khan Academy (https://www.khanacademy.org/math/statistics-probability/displaying-describing-data) and Udacity (https://classroom.udacity.com/courses/st101/) courses.
