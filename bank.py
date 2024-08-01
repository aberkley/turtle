import math


HELENA_BALANCE = 1100

SOFIA_BALANCE = 1300


def figure_out_interest(cash_at_start, interest_rate, number_of_weeks):
    CASH_AT_START = cash_at_start
    cash_at_end = CASH_AT_START
    for week in range(number_of_weeks):
        cash_at_start = cash_at_end
        if cash_at_start > 1000:
            first_interest = 1000 * interest_rate
            remaining_interest = (cash_at_start - 1000) * interest_rate * 0.5
            interest = first_interest + remaining_interest
        else:
            interest = cash_at_start * interest_rate
        cash_at_end = interest + cash_at_start
    interest_owed = cash_at_end - CASH_AT_START
    interest_owed = math.ceil(interest_owed)
    return {'interest': interest_owed, 'balance_at_end': math.ceil(cash_at_end)}


data = figure_out_interest(SOFIA_BALANCE, 2 / 100, 35)
print(data)