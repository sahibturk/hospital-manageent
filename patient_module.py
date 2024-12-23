from db_connector import get_connection  # Import the database connection function
from mysql.connector import Error  # Import Error handling for MySQL

class PatientManager:
    @staticmethod
    def add_patient():
        """
        Adds a new patient to the Patients table in the database.
        """
        try:
            # Gather patient details from user input
            name = input("Enter patient name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender (Male/Female/Other): ")
            address = input("Enter address: ")
            contact = input("Enter contact number: ")

            # Establish a database connection
            connection = get_connection()
            cursor = connection.cursor()

            # SQL query to insert patient details into the table
            query = """INSERT INTO Patients 
                       (name, age, gender, address, contact, admission_date) 
                       VALUES (%s, %s, %s, %s, %s, CURDATE())"""
            cursor.execute(query, (name, age, gender, address, contact))

            # Commit the transaction
            connection.commit()
            print("Patient added successfully.")

        except Error as e:
            # Handle database-related errors
            print(f"Database Error: {e}")

        except ValueError:
            # Handle incorrect input types (e.g., non-integer age)
            print("Invalid input. Please enter the correct data type.")

        finally:
            # Close the database connection
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Connection closed.")

    @staticmethod
    def view_all_patients():
        """
        Retrieves and displays all patients from the database.
        """
        try:
            # Establish a database connection
            connection = get_connection()
            cursor = connection.cursor()

            # SQL query to fetch all patients
            query = "SELECT * FROM Patients"
            cursor.execute(query)
            results = cursor.fetchall()

            # Display patients in a tabular format
            print("Patient Records:")
            print("ID | Name       | Age | Gender | Address      | Contact     | Admission Date")
            print("-" * 80)
            for row in results:
                print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<3} | {row[3]:<6} | {row[4]:<12} | {row[5]:<10} | {row[6]}")

        except Error as e:
            # Handle database-related errors
            print(f"Database Error: {e}")

        finally:
            # Close the database connection
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Connection closed.")
