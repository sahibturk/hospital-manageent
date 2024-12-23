from db_connector import get_connection

class BillingManager:
    @staticmethod
    def generate_bill():
        patient_id = int(input("Enter patient ID: "))
        treatment_details = input("Enter treatment details: ")
        total_amount = float(input("Enter total amount: "))

        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Bills (patient_id, treatment_details, total_amount, billing_date) VALUES (%s, %s, %s, CURDATE())"
        cursor.execute(query, (patient_id, treatment_details, total_amount))
        connection.commit()
        print("Bill generated successfully.")
        connection.close()

    @staticmethod
    def view_bills():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Bills")
        for bill in cursor.fetchall():
            print(bill)
        connection.close()

    @staticmethod
    def manage():
        print("1. Generate Bill")
        print("2. View Bills")
        choice = int(input("Choose an option: "))
        if choice == 1:
            BillingManager.generate_bill()
        elif choice == 2:
            BillingManager.view_bills()


