#Medical_Hospital Programme
def inpatients(number_of_days,daily_rate,Hospital_medication_charges,Service_cherges):
    Total_Charges=(number_of_days*daily_rate)+Service_cherges+Hospital_medication_charges
    return Total_Charges
# Out patient Function this calculates the total Amount    
def outpatient(Service_cherges,Hospital_medication_charges):
 Total_charges=Service_cherges+Hospital_medication_charges
 return Total_charges
 
#  The main Function will be used by the User enter data   
def main():
 Choices=int(input("CHOOSE 1.in-patients\n 2.Outpatients")) 
# Control if statement will be used to enable Branching in our Code
 if Choices==1:
    print("inpatients Services")
    number_of_days=int(input("Enter the Number of Days"))
    daily_rate=float(input("Enter the daily rate"))
    Service_cherges=float(input("Enter the Service charges"))
    Hospital_medication_charges=float(input("Enter the Hospital Medicattion charges"))
    print("Total bill:",inpatients(number_of_days,daily_rate,Service_cherges,Hospital_medication_charges))
 elif Choices==2:
     print("Out-Patients Programme")
     Service_cherges=float(input("Enter the Service Charges(Lab test etc..)"))
     Hospital_medication_charges=float(input("Enter the Hospital medication Services"))
     print("Total Bill:",outpatient(Service_cherges,Hospital_medication_charges))
    
main()
    
