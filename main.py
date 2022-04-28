"""
In this project, I am going to be creating a program that is going to take all the inputs associated with an
internships and calculate my entire pay with taxes in Arizona.

My inputs that I am going to ask for are as follows:
- What is the hourly rate that you will be receiving for this internship?
- How many hours will you be working in one day during this internship?
- How many days in a week will you be working? (*Note* : This number will be out of 5 not 7 as weekends do not count.)
- What is the total number of weeks you will be working for this internship?
"""

hourly_rate = int(input("\nWhat is the hourly rate that you will be receiving for this internship? : $ "))
hours_in_working_day = int(input("\nHow many hours will you be working in one day during this internship? : "))
days_in_a_week_working = int(input("\nHow many days in a week will you be working? "
                               "\n (*Note* : This number will be out of 5 not 7 as weekends do not count.) : "))
total_num_of_weeks = int(input("\nWhat is the total number of weeks you will be working for this internship? : "))

money_for_one_day = hourly_rate * hours_in_working_day
print("\nWith an hourly rate of $" + str(hourly_rate) + " and by working " + str(hours_in_working_day) + " hours a day, "
                                                                                            "you will make $" +
      str(money_for_one_day) + " a day!")

money_for_one_week = money_for_one_day * days_in_a_week_working
print("\nBy making $" + str(money_for_one_day) + " a day and working " + str(days_in_a_week_working) + " days in a week,"
                                                                                                       " you will be making $"
      + str(money_for_one_week) + " in one week!")

money_for_total_num_of_weeks = money_for_one_week * total_num_of_weeks
print("\nBy making $" + str(money_for_one_week) + " in one week, you will be making $" + str(money_for_total_num_of_weeks) +
      " in " + str(total_num_of_weeks) + " weeks!")

tax_amount_taken_from_total = 0.09 * money_for_total_num_of_weeks
print("\nAs Arizona has tax rates of 2.59 % to 9.00 %, I took the largest tax rate just for worst case scenario "
      "\nwhich is 9.00 %. Then I multiplied that tax rate with the total amount of money for the internship to find"
      "\nout how much will be deducted from the total which is $" + str(tax_amount_taken_from_total) + "!")

complete_total_after_taxes = money_for_total_num_of_weeks - tax_amount_taken_from_total
print("\nAfter deducting the tax amount, you will be receiving $" + str(complete_total_after_taxes) + "!")