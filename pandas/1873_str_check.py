# Write a solution to calculate the bonus of each employee. 
# The bonus of an employee is 100% of their salary if the ID of the employee is an odd number 
# and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

# The result format is in the following example.

# Example 1:

# Input: 
# Employees table:
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+
# Output: 
# +-------------+-------+
# | employee_id | bonus |
# +-------------+-------+
# | 2           | 0     |
# | 3           | 0     |
# | 7           | 7400  |
# | 8           | 0     |
# | 9           | 7700  |
# +-------------+-------+
# Explanation: 
# The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
# The employee with ID 3 gets 0 bonus because their name starts with 'M'.
# The rest of the employees get a 100% bonus.

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees[(employees.employee_id % 2 == 1) & (~employees.name.str.startswith('M'))]['salary']
    employees['bonus'] = employees['bonus'].fillna(0)
    return employees[['employee_id', 'bonus']].sort_values('employee_id')

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})
print(calculate_special_bonus(Employees))