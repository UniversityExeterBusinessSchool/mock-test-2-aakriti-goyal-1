#######################################################################################################################################################
# 
# Name: Aakriti Goyal
# SID: 740099010
# Exam Date: 28/03/2025
# Module: Programming for Business Analytics
# Github link for this assignment:  
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
average_sales= sum(weekly_sales)/len(weekly_sales)
for i in range(len(weekly_sales)):
    sales = weekly_sales[i]    
    if sales > average_sales:
        print("Week ",i+1,"sales are above average")
    else:
        print("Week ",i+1,"sales are below average")

#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.
word1 = "good"
word2 = "improved"
word1_start = customer_feedback.find(word1)
word2_start = customer_feedback.find(word2)
my_list = []
word1_end = word1_start + len(word1)
word2_end = word2_start + len(word2)
my_list.append((word1_start,word1_end))
my_list.append((word2_start,word2_end))
print(my_list)
#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.


# 1. Net Profit Margin = (Net Profit / Revenue) * 100
def net_profit_margin(net_profit, revenue):
    return (net_profit / revenue) * 100

# 2. Customer Acquisition Cost (CAC) = Total Marketing Cost / New Customers Acquired
def customer_acquisition_cost(marketing_cost, new_customers):
    return marketing_cost / new_customers

# 3. Net Promoter Score (NPS) = (Promoters - Detractors) / Total Respondents * 100
def net_promoter_score(promoters, detractors, total_respondents):
    return ((promoters - detractors) / total_respondents) * 100

# 4. Return on Investment (ROI) = (Net Gain from Investment / Investment Cost) * 100
def return_on_investment(net_gain, investment_cost):
    return (net_gain / investment_cost) * 100


# Sample values using SID digits
net_profit = 7400   
revenue = 15000     

marketing_cost = 7400
new_customers = 10

promoters = 74
detractors = 10
total_respondents = 100

net_gain = 1500
investment_cost = 7400

# Print results
print("Net Profit Margin:", round(net_profit_margin(net_profit, revenue), 2), "%")
print("Customer Acquisition Cost:", round(customer_acquisition_cost(marketing_cost, new_customers), 2))
print("Net Promoter Score:", round(net_promoter_score(promoters, detractors, total_respondents), 2), "%")
print("Return on Investment (ROI):", round(return_on_investment(net_gain, investment_cost), 2), "%")

#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
df = pd.DataFrame(sales_data)
print("Original Sales Data: ")
print(df)
df['Cumulative Sales'] = df['Sales'].cumsum()
print("Sales Data with Cumulative Sales:")
print(df)
#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Define data
price = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1, 1)
demand = np.array([200, 180, 170, 160, 150, 140, 130])

# Step 2: Fit the linear regression model
model = LinearRegression()
model.fit(price, demand)

# Step 3: Predict demand at price £26
predicted_demand = model.predict(np.array([[26]]))
print(f"Predicted demand at £26: {round(predicted_demand[0])} units")

# Step 4: Plotting
# Generate predicted demand for all prices to draw regression line
price_range = np.linspace(15, 30, 100).reshape(-1, 1)
demand_predicted = model.predict(price_range)

# Scatter plot of actual data
plt.scatter(price, demand, color='blue', label='Actual Data')

# Regression line
plt.plot(price_range, demand_predicted, color='red', linestyle='--', label='Regression Line')

# Highlight the prediction for £26
plt.scatter(26, predicted_demand, color='green', label='Prediction at £26')

# Labels and legend
plt.title("Price vs Demand with Regression Line")
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.legend()
plt.grid(True)
plt.show()


#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
def calculate_total(prices_dict):
    total = 0
    for item, price in prices_dict.items():
        try:
            total += float(price)  # Try converting to float (to handle int or float)
        except (ValueError, TypeError):
            # If price is not a number, print a warning and skip it
            print(f"Warning: Skipping item '{item}' with invalid price '{price}'")
    return total

# Dictionary of prices
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Call the function and print result
total_price = calculate_total(prices)
print(f"\nTotal valid price: {total_price}")

# Include error handling in your function and explain where and why it’s needed.

#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random

# Step 1: Generate 50 random numbers between 1 and 500
random_numbers = [random.randint(1, 500) for _ in range(50)]

# Step 2: Plot a histogram
plt.hist(random_numbers, bins=10, color='skyblue', edgecolor='black')

# Step 3: Add labels and title
plt.title("Histogram of 50 Random Numbers")
plt.xlabel("Number Range")
plt.ylabel("Frequency")

# Step 4: Display the plot
plt.grid(True)
plt.show()

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
doubled_quantities = [q * 2 for q in quantities if q >= 10]
# Print the original and the new lists.
print("Original quantities:", quantities)
print("Doubled (10 or more):", doubled_quantities)


#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

# Filter the dictionary to include only products with rating >= 4
high_rated_products = {product: rating for product, rating in ratings.items() if rating >= 4}

# Print the result
print("Filtered Products (Rating >= 4):")
print(high_rated_products)

#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = total / len(values)
print("The average is = " + str(average))

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

#######################################################################################################################################################
