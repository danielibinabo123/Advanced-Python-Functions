marks=[85, 92, 78, 96, 88]
percentages=[(x/100)*100 for x in marks]
print(percentages)

students=["Alice", "Bob", "Charlie", "David", "Eva"]
outcome={name: pct for name, pct in zip(students, percentages)}
print(outcome)

salary_dollar=[2000, 2500, 3000, 4000, 3500]
salary_naira=list(map(lambda x: x * 1300, salary_dollar))

print(salary_naira)