import pickle

sort_dict = {}

with open('data.csv', 'r') as file:
    headers = file.readline().strip().split(', ')

    for line in file:
        values = line.strip().split(', ')
        student_data = {headers[i]: values[i] for i in range(len(headers))}
        grade = student_data['Grade']
        language = student_data['Prog. Language']
        if grade not in sort_dict:
            sort_dict [grade] = {}
        if language not in sort_dict [grade]:
            sort_dict [grade][language] = []
        student_info = {
            'No': student_data['No'],
            'Student': student_data['Student'],
            'Age': student_data['Age'],
            'Sex': student_data['Sex']
        }
        sort_dict [grade][language].append(student_info)

with open('sort_dict.pkl', 'wb') as byte_file:
    pickle.dump(sort_dict, byte_file)

