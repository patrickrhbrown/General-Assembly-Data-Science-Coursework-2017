import pickle
import numpy as np
import scipy.stats as scs
import math

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A array of numbers for the exercise]
    """
    return pickle.load(open(file_name))


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The array containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A array that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    sample = np.random.choice(population, n)
    return(sample)

    pass


def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The array of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    #declare a variable raw_mean that is the sum of
    #all values in the list, divided by the length
    #of the list. We cast the list value to a float
    #so that decimal fractions don't throw the accuracy
    #of our mean by rounding up or down
    mean_value = sum(lst) / float(len(lst))
    #we return the value of raw_mean as the output
    return(float(mean_value))

    pass


def get_variance(lst, sample=False):
    """INPUT:
    - lst(NUMPY ARRAY) [Either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    if not sample:
        n=len(lst)
        mean_value = sum(lst) / n
        variance = sum([(i - mean_value)**2 for i in lst]) / n
        return(variance)
    else:
        mean_value = sum(lst) / len(lst)
        n = len(lst) - 1
        variance = sum([(i - mean_value)**2 for i in lst]) / n
        return(variance)
    pass


def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    """

    n = len(sample) - 1
    mean_value = sum(sample) / float(len(sample))
    variance = sum([(i - mean_value)**2 for i in sample]) / n
    sem = math.sqrt(variance) / math.sqrt(len(sample))
    return(sem)

    pass


if __name__ == '__main__':
    population = load_pickle('../data/population.pkl')
    print 'First 10 element of the population: ', population[:5]
    sample_100 = draw_sample(population, 100)
    sample_1000 = draw_sample(population, 1000)
    sem_100 = get_sem(sample_100)
    sem_1000 = get_sem(sample_1000)
    print('Mean of the population:')
    print(get_mean(population))
    print('Mean of the sampled 100:')
    print(get_mean(sample_100))
    print('Mean of the sampled 1000:')
    print(get_mean(sample_1000))
    print('Variance of the Population:')
    print(get_variance(list(population), sample=False))
    print('Variance of the Sampled 100:')
    print(get_variance(sample_100, sample=True))
    print('Variance of the Sampled 1000:')
    print(get_variance(sample_1000, sample=True))
    print('SEM of the Sampled 100:')
    print(sem_100)
    print('SEM of the Sampled 1000:')
    print(sem_1000)
