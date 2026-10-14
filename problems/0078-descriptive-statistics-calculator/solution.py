import numpy as np
import math 
def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here

    d = np.array(data)
    mean = d.mean()

    median = 0
    if(len(d) % 2 ==0):
        mid = len(d) // 2
        median = (d[mid] + d[mid-1]) / 2
    else:
        median = d[len(d)//2]

    mode = 0
    apps = {}
    for i in d:
        if(i in apps):
            apps[i] = apps[i]+1
        else:
            apps[i] = 1
    c=0

    for n in apps:
        if apps[n] > c:
            mode = n
            c = apps[n]

    varianza = 0

    for n in d:
        varianza += (n - mean) ** 2
    varianza /= len(d)

    std = varianza ** 0.5

    #cuantiles
    def cal_q(k, n):
        return (k * (n+1)) / 100

    length = len(d)
    p25 = cal_q(25, length)

    entera = int(p25)
    dec = p25-entera

    perc25th = 0
    if(math.isclose(dec, 0.0, abs_tol=1e-9)):
        perc25th = d[entera-1]
    else:
        perc25th = d[entera-1]  + dec +(d[entera]-d[entera-1])


    p50 = cal_q(50, length)
    entera = int(p50)
    dec = p50-entera

    perc50th = 0
    if(math.isclose(dec, 0.0, abs_tol=1e-9)):
        perc50th = d[entera-1]
    else:
        perc50th = d[entera-1]  + dec +(d[entera]-d[entera-1])

    p75 = cal_q(75, length)

    output = {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': varianza,
        'standard_deviation': std,
        '25th_percentile': np.percentile(d, 25), 
        '50th_percentile': np.percentile(d, 50), 
        '75th_percentile':np.percentile(d, 75),
        'interquartile_range': np.percentile(d, 75) - np.percentile(d, 25)

    }
    return output