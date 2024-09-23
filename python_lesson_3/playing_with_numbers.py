money_start = float(input("How much will you be saving every year? "))
saving_years = float(input("For how many years will you be saving? "))
interest_rate = float(input("How much will you be adding to your savings? "))
money_result = money_start*interest_rate*saving_years
print("Your savings after " + str(saving_years) + " years: $"+ str(money_result))
print("Will you be able to renovate home library? " + str(money_result>10000))