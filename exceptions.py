my_dict = {'name': 'Jack', 'age': 27, 'sex': ['M']}

try:
    sex = my_dict['sex']
    sex_de = sex + 3
except KeyError:
    print("exception occurred")
except TypeError as e:
    print("type error occurred")
    print(e)

print("Code executed")