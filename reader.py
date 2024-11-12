import pickle
import os

with open('sort_dict.pkl', 'rb') as byte_file:
    loaded_dict = pickle.load(byte_file)

main_folder = 'students_data'

os.makedirs(main_folder, exist_ok=True)

def save_data_to_folders(data_dict, main_folder):
    for grade, languages in data_dict.items():
        grade_folder = os.path.join(main_folder, f"Grade_{grade}")
        os.makedirs(grade_folder, exist_ok=True)
        grade_file_path = os.path.join(grade_folder, f"{grade}_students.txt")
        with open(grade_file_path, "w", encoding="utf-8") as file:
            file.write(f"Студенти для Grade {grade}:\n")
            for language, students in languages.items():
                file.write(f"\nProgramming Language: {language}\n")
                for student in students:
                    file.write(
                        f"  No: {student['No']}, Student: {student['Student']}, Age: {student['Age']}, Sex: {student['Sex']}\n"
                    )
    print(f"Дані успішно збережені у структурованій папці '{main_folder}'.")

save_data_to_folders(loaded_dict, main_folder)

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
                    f"    No: {student['No']}, Student: {student['Student']}, Age: {student['Age']}, Sex: {student['Sex']}"
                )
print("\nVisualizing all data:")
visualize_data()
