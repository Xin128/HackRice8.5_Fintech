import pandas
import numpy as np



def compute_increase_rate(input_data):
    """
    This function computes the increase rate for the input data
    :param input_data: a dictionary that contains the stock prices for each company
    :return: a list that contains the increasing rate of stock price every day
    """
    rates = {}
    for comp in input_data:
        stock_prices = input_data[comp][1]
        rates[comp] = []
        for i in range(len(stock_prices)-1):
            # Add a new increase rate to the dictionary
            rates[comp].append((stock_prices[i] - stock_prices[i+1])/stock_prices[i+1])
    return rates

def compute_zscore(input_data, comp_name):
    """
    Compute the z-score for a group of data
    :param input_data: the rate the stock prices increase for every day
           comp_name: the name of the company
    :return: the zscore for the data
    """
    try:
        input_data = np.array(input_data[comp_name])
    except KeyError:
        print("The company is not included in our database")
        return False
    # Initialize the z-score list
    zscore = []
    # For each piece of data, compute its z-score
    for i in range(len(input_data)):
        daily_zscore = (input_data[i] - np.mean(input_data))/np.std(input_data)
        zscore.append(daily_zscore)
    return zscore

def fin_advice(input_data, comp_name):
    """
    This return the advice that whether we should keep the stock, sell it, or buy it
    :param input_data: Alex's style of data for the company
           comp_name: the name of the company
    :return: What should the user do to their stock
    """
    # Compute the Z-score for a certain company
    inc_rate = compute_increase_rate(input_data)
    zscore = compute_zscore(inc_rate, comp_name)
    if zscore == False:
        return None
    if zscore[-1] > 1:
        return "You should sell" + "Z-Score: " + str(zscore)
    elif zscore[-1] < -1:
        return "You should buy" + "Z-Score: " + str(zscore)
    else:
        return "You should keep" + "Z-Score: " + str(zscore)








def return_rise(companies):
    """

    :param companies: given dictionary
    :return: companies that have rise in stock price percentage
    """
    rise_company_and_percentrage = {}
    for company, data in companies.items():
        if data[0]>0:
            rise_company_and_percentrage[company] = data[0]
    return rise_company_and_percentrage

def return_fall(companies):
    """

    :param companies: given dictionary
    :return: companies that have fall in stock price percentage
    """
    fall_company_and_percentrage = {}
    for company, data in companies.items():
        if data[0] < 0:
            fall_company_and_percentrage[company] = data[0]
    return fall_company_and_percentrage

def highest_rise(rise_company):
    """

    :param rise_company: dictionary result from return_rise
    :return: the highest rise company
    """
    max = 0
    max_company = None
    for company, percentage in rise_company.items():
        if percentage[0] > max:
            max = percentage
            max_company = company
    return (max_company, max)

def highest_fall(fall_company):
    """

    :param rise_company: dictionary result from return_fall
    :return: the highest fall company
    """
    min = (0,0)
    min_company = None
    for company, percentage in fall_company.items():
        if percentage[0] < min[0]:
            min = percentage
            min_company = company
    return (min_company, min)

def month_average(companies):
    """
    compute monthly average for each company
    :param companies: given dictionary
    :return: a dictionary where key is name of the company and value is the average stock price
    """
    company_average = {}
    for company, data in companies.items():
        sum = 0
        for price in data[1]:
            sum += price
        company_average[company] = sum/len(data[1])

    return company_average
