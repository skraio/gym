'''
Write a solution to fix the names so that only the first character is 
uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The result format is in the following example.

Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
'''
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    return users.assign(name = users['name']\
                               .str\
                               .capitalize())\
                               .sort_values(by = 'user_id', ascending = True)