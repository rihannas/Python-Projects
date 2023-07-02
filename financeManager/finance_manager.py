#!/usr/bin/python3
"""

This module sorts csv file by date and calculates the yearly and monthly costs through a csv file.
"""
import pandas
import csv


months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May",
          6: "Jun"}
costs = []


def orderbyMonth(file):

    with open(file, 'r') as csv_file:
        df = pandas.read_csv(csv_file)
    # displaying unsorted data frame
    df.sort_values(by=['month'], ascending=[True], axis=0, inplace=True)
    df.to_csv("orderedbyMonth.csv", index=False)


def monthly(file, month):
    # get month in num
    for k, v in months.items():
        if v == month:
            numMonth = k

    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # skip the top row (which is headers)
        for row in csv_reader:
            # get the month
            date = row[1]
            year, mon = date.split('-')
            mon = int(mon)

            # get the expenses row
            # to convert to float, i need to remove anything characters that can't be float
            cost = float(row[3].strip("$"))
            if mon == numMonth:
                costs.append(cost)

    total = sum(costs)

    return "The total expenses for {}: ${:.2f}".format(month, total)


def yearly(file, year):
    # get month in num

    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # skip the top row (which is headers)
        for row in csv_reader:
            # get the month
            date = row[1]
            yea, mon = date.split('-')
            yea = int(yea)
            # get the expenses row
            # to convert to float, i need to remove anything characters that can't be float
            cost = float(row[3].strip("$"))
            if year == yea:
                costs.append(cost)

    total = sum(costs)

    return "The total expenses for {}: ${:.2f}".format(yea, total)


monthly_report = monthly('orderedbyMonth.csv', "Jan")
print(monthly_report)

yearly_report = yearly('orderedbyMonth.csv', 2022)
print(yearly_report)
