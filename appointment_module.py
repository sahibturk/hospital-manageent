# appointment_module.py
from db_connector import get_connection

class AppointmentManager:

    @staticmethod
    def add_appointment():
        # Input for patient and doctor ID, and appointment date
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ")

        # Establishing connection to the database
        connection = get_connection()
        cursor = connection.cursor()
        
        # SQL query to insert the appointment
        query = """INSERT INTO Appointments (patient_id, doctor_id, appointment_date)
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (patient_id, doctor_id, appointment_date))
        
        # Committing the transaction
        connection.commit()
        print("Appointment scheduled successfully.")
        
        # Closing the connection
        connection.close()

    @staticmethod
    def view_appointments():
        # Establishing connection to the database
        connection = get_connection()
        cursor = connection.cursor()
        
        # SQL query to fetch appointments
        query = """SELECT appointment_id, p.name AS patient_name, d.name AS doctor_name, a.appointment_date
                   FROM Appointments a
                   JOIN Patients p ON a.patient_id = p.id
                   JOIN Doctors d ON a.doctor_id = d.id"""
        cursor.execute(query)
        
        # Fetching all the results from the query
        results = cursor.fetchall()
        print("Appointments:")
        
        # Displaying the results
        for row in results:
            print(f"Appointment ID: {row[0]}, Patient Name: {row[1]}, Doctor Name: {row[2]}, Appointment Date: {row[3]}")
        
        # Closing the connection
        connection.close()
