import numpy as np
import scipy.stats as scs


def get_mean(lst):
#declare a variable raw_mean that is the sum of
#all values in the list, divided by the length
#of the list. We cast the list value to a float
#so that decimal fractions don't throw the accuracy
#of our mean by rounding up or down
    raw = sum(lst) / float(len(lst))
#we return the value of raw_mean as the output
    return(float(raw))

    """Return the mean of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, mean value of the input list

    Do not use np.mean().
    """

    pass


def get_median(lst):
    """Return the median of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, median value of the input list

    Do not use np.median().
    """
        #we use map to cast all items in the list to floats
    data = map(float, lst)
    #we declare a variable n that is the length of our list of floats
    n = len(data)
    #we sort our list of values in size order
    data.sort()
    # Test whether n is odd by checking if there is a remainder if divided by two
    if n % 2 != 0:
    # If n == odd, get the index simply by dividing it in half
        result = n/2
    else:
        # If n (length of data) is even, average the two values at the center
        high_limit = n / 2
        lower_limit = n / 2 - 1
        result = (data[lower_limit] + data[high_limit]) / 2
    return(float(result))
    pass


def get_mode(lst):
    """Return the mode of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, mode value of the input list (FLOAT)

    Do not use scs.mode().
    """
    m = max([lst.count(val) for val in lst])
    return [x for x in lst if val.count(x) == m][0] if m>1 else None

    pass


def get_range(lst):
    """Return the range of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, range of the input list
    """

    #we sort the list in order of magnitude
    lst.sort
    #we declare a variable got_range that subtracts the max of the list from min
    got_range = max(lst) - min(lst)
    #we return the result
    return(got_range)
    pass


def get_IQR(lst):
    """Return the interquartile range of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, interquartile range of the input list (FLOAT)

    Hint: you may use np.percentile
    """

    #we call np.percentile, passing in the list of percentiles we want
    # in order to calculate the interquartile range
    #and pass the result to a tuple
    twenty_five,seventy_five = np.percentile(lst,[25,75])
    #we assign the result of subtracting the 75th percentile
    #from the 25th percentile and assign it to the variable IQR
    IQR = seventy_five - twenty_five
    #we return the result as the product of the function
    return IQR

    pass


def remove_outliers(lst):
    """Return all the values in lst in sorted order without the outliers

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    list, sorted lst with any data points 3 interquartile range below Q1
    (25th percentile) or 3 interquartile range above Q3 (75th percentile)
    """
    twenty_five,seventy_five = np.percentile(lst,[25,75])
    #we assign the result of subtracting the 75th percentile
    #from the 25th percentile and assign it to the variable IQR
    IQR = seventy_five - twenty_five
    final_list = lst.sort
    final_list = [x for x in lst if (x > 3 * IQR)]
    final_list = [x for x in final_list if (x < 3 * IQR)]
    final_list_sorted = final_list.sort
    return(final_list_sorted)
    pass


def run_check(lst):
    """Check the output of functions implemented (mean, median and mode)

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    None, prints out the results of the test comparing hand implemented
        functions to corresponding 'np' or 'scs' methods.
    """
    print('Mean: ', get_mean(lst) == np.mean(lst))
    print('Median: ', get_median(lst) == np.median(lst))
    print('Mode: ', get_mode(lst) == scs.mode(lst).mode[0])


def print_summary_metrics(lst):
    """Print an overview of all summary statistics mentioned in this exercise

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    None, prints out the values of the summary statistics studied in
        this exercise.
    """
    print('*' * 50)
    print(' ' * 16 + 'Summary statistics')
    print('*' * 50)
    print('mean: {} | median: {} | mode: {}'.format(get_mean(lst),
                                                    get_median(lst),
                                                    get_mode(lst)))
    print('range: {} | IQR: {}'.format(get_range(list_nums),
                                       get_IQR(list_nums)))
    print('\n')
    print('original list: \n          {}'.format(lst))
    print('sorted list: \n          {}'.format(sorted(lst)))
    print('List without outliers: \n          {}'.format(
                                                remove_outliers(list_nums)))


if __name__ == '__main__':
    list_nums = [100, 9, 4, 7, 22, 37, 44, 22, 79, 88, 200, 37, 22, 1000]
    run_check(list_nums)
    print_summary_metrics(list_nums)
