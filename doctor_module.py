from db_connector import get_connection

class DoctorManager:
    @staticmethod
    def add_doctor():
        name = input("Enter doctor name: ")
        specialization = input("Enter specialization: ")
        
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Doctors (name, specialization, availability) VALUES (%s, %s, TRUE)"
        cursor.execute(query, (name, specialization))
        connection.commit()
        print("Doctor added successfully.")
        connection.close()

    @staticmethod
    def view_doctors():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Doctors")
        for doctor in cursor.fetchall():
            print(doctor)
        connection.close()

    @staticmethod
    def manage():
        print("1. Add Doctor")
        print("2. View Doctors")
        choice = int(input("Choose an option: "))
        if choice == 1:
            DoctorManager.add_doctor()
        elif choice == 2:
            DoctorManager.view_doctors()
