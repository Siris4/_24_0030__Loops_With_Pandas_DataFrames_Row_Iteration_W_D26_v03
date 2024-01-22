student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

print(student_dict)

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
'''
{'student': ['Angela', 'James', 'Lily'], 'score': [56, 76, 98]}
['Angela', 'James', 'Lily']
[56, 76, 98]
  student  score
0  Angela     56
1   James     76
2    Lily     98
'''


# Looping through a Data Frame:
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)
'''
0    Angela
1     James
2      Lily
Name: student, dtype: object
score
0    56
1    76
2    98
Name: score, dtype: int64
'''

# Loop through rows of a Data Frame:
for (index, row) in student_data_frame.iterrows():
    print(f"row = {row}\n")
    print(f"index = {index}\n")
    print(f"row.student = {row.student}\n")  #each of these rows is going to be a Pandas Series object.
    print(f"row.score = {row.score}\n")
    if row.student == "Angela":    #since each of these rows is going to be a Pandas Series object, we can utilize the . functionality with "row.student" and also...
        print(f"if Angela, row.score = {row.score}\n")   # row.score.    If "Angela", then print that same row we are iterating over, print that score.

'''
Results of FULL code being ran:
{'student': ['Angela', 'James', 'Lily'], 'score': [56, 76, 98]}
['Angela', 'James', 'Lily']
[56, 76, 98]
  student  score
0  Angela     56
1   James     76
2    Lily     98
row = student    Angela
score          56
Name: 0, dtype: object

index = 0

row.student = Angela

row.score = 56

if Angela, row.score = 56

row = student    James
score         76
Name: 1, dtype: object

index = 1

row.student = James

row.score = 76

row = student    Lily
score        98
Name: 2, dtype: object

index = 2

row.student = Lily

row.score = 98
'''