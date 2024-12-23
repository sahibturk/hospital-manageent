from patient_module import PatientManager
from doctor_module import DoctorManager
from appointment_module import AppointmentManager
from billing_module import BillingManager

def main():
    while True:
        print("\nHospital Management System")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Manage Appointments")
        print("4. Manage Billing")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("1. Add Patient\n2. View All Patients")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                PatientManager.add_patient()
            elif sub_choice == "2":
                PatientManager.view_all_patients()
            else:
                print("Invalid choice.")

        elif choice == "2":
            print("1. Add Doctor\n2. View All Doctors")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                DoctorManager.add_doctor()
            elif sub_choice == "2":
                DoctorManager.view_all_doctors()
            else:
                print("Invalid choice.")

        elif choice == "3":
            print("1. Schedule Appointment\n2. View All Appointments")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                AppointmentManager.add_appointment()
            elif sub_choice == "2":
                AppointmentManager.view_appointments()
            else:
                print("Invalid choice.")

        elif choice == "4":
            print("1. Generate Bill\n2. View All Bills")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                BillingManager.generate_bill()
            elif sub_choice == "2":
                BillingManager.view_bills()
            else:
                print("Invalid choice.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
