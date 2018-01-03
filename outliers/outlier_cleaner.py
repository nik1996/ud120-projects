#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    from operator import itemgetter

    ### your code goes here
    for i in range(len(predictions)):
        age,net_worth,error = ages[i],net_worths[i],abs(predictions[i]-net_worths[i])
        cleaned_data.append((age,net_worth,error))
    cleaned_data.sort(key=itemgetter(2))

    cleaned_data = cleaned_data[:-9]
    return cleaned_data
