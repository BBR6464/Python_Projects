# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)
# import random
#
# names = ['Alex', 'Bath', 'Dave', 'Caroline', 'Eleanor', 'Freddie']
# student_score = {student:random.randint(3, 100) for student in names}
# passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
# print(passed_students)


# sentence = input()
# # 🚨 Don't change code above 👆
# # Write your code below 👇
# result = {word: len(word) for word in sentence.split()}
# print(result)


# weather_c = eval(input())
# # 🚨 Don't change code above 👆
# # Write your code 👇 below:
# weather_f = {word:(item * 9/5) + 32 for (word, item) in weather_c.items()}
# print(weather_f)


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)
# #
# # #Loop through a data frame
# # for (key,  value) in student_data_frame.items():
# #     print(value)
#
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)

