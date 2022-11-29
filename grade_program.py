#!/usr/bin/env python3
# Created by: Patrice Pat-Odita
# Created on: Nov 28, 2022
# This program uses a switch case function to determine the middle percentage
# grade level.this program asks user to input a grade level
# and returns associated  middle percentage.


def calc_mark(level):
    # using an if  else statement to match up the levels with the percents
    if level == "4++":
        percent = "110%"
    elif level == "4+":
        percent = "98%"
    elif level == "4":
        percent = "90%"
    elif level == "4-":
        percent = "83%"
    elif level == "3+":
        percent = "78%"
    elif level == "3":
        percent = "75%"
    elif level == "3-":
        percent = "71%"
    elif level == "2+":
        percent = "68%"
    elif level == "2":
        percent = "65%"
    elif level == "2-":
        percent = "61%"
    elif level == "1+":
        percent = "58%"
    elif level == "1":
        percent = "55%"
    elif level == "1-":
        percent = "51%"
    elif level == "R":
        percent = "Percent is less than 50%"
    else:
        percent = "invalid"

    return percent


def main():
    # get user input
    grade = input("Enter the grade level: ")
    # setting a variable to the return value of calc_grade
    calculated_grade = calc_mark(grade)
    # displays the results
    if calculated_grade == "level inputted was invalid":
        print(calculated_grade)
    else:
        print("The middle percent of {} is {}.".format(grade, calculated_grade))


if __name__ == "__main__":
    main()
