import pickle

with open('sort_dict.pkl', 'rb') as byte_file:
    loaded_dict = pickle.load(byte_file)

def visualize_data(grade=None, language=None):
    for g, languages in loaded_dict.items():
        if grade and g != grade:
            continue
        print(f"Grade {g}:")
        for lang, students in languages.items():
            if language and lang != language:
                continue
            print(f"  Programming Language {lang}:")
            for student in students:
                print(
                    f"    No: {student['No']}, Student: {student['Student']}, Age: {student['Age']}, Sex: {student['Sex']}")
print("\nVisualizing all data:")
visualize_data()
