has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan.")

if has_high_income or has_good_credit:
    print("Eligible for loan.")

if has_good_credit and not has_criminal_record:
    print("NOT: Eligible for loan.")

"""
if applicant has high income AND good credit
    Eligible for loan

# NOT
if applicant has good credit AND doesn't have a criminal record
    Eligible for loan

In logical operator, we have 3 types of operators:
- AND: it will show result when both conditions are TRUE
- OR: it will show result when one of the conditions are TRUE
- NOT: it will reverse the result that we receive, such as TRUE to FALSE and vice versa.
"""