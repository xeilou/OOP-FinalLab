class Add_Student:

    def __init__(self, student):
        self.student_data = student

    def write_student_info(self, name, age, id_num, email, phone_num):
        file = open('student_data.txt','a')

        file.write(name + '\t')
        file.write(age + "\t")
        file.write(id_num + "\t")
        file.write(email + "\t")
        file.write(phone_num + "\n")

    def add_student(self, name, age, id, email, phone):
        student = [name, age, id, email, phone]
        self.student_data.student_list.append(student)
        print(f"Added Student {student[0]} to the list.")

        self.write_student_info(name, age, id, email, phone)