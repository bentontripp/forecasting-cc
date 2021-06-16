## Introduction & Overview

Forecasting for a Call Center has proven to be more complex than I first thought - and my methods continue to develop and change as I learn or find new ideas.

For example, something that I would like to implement eventually are a few additional variables in my random forest regression model: number of letters sent to customers, days since letters were last sent, and number of active member accounts.

There are two methods I have included. The first is a classic Time-Series using a weighted moving average. This model forecasts based on day of week and increases the forecast by a fixed amount on the days following a holiday. The methodology has proven effective, although some manual adjustments are occasionally needed. There are also a group of employees that occasionally assist one of the departments, and their handle time needed to be excluded in the forecasts in order for the business to understand what was actually happening.

The second method was Random Forest Regression. I did not include my work of tuning the hyperparameters (although I did include the function that I created to do this). This method seems to be at least as accurate if not more than the original Time Series - but can be somewhat unpredictable for the smaller departments.

Both models are pulling from data in an excel BI report generated daily that includes a tab for number of calls (volume) and handle time (aht). They both also look at some shared variables to distinguish holidays and departments/groups.
