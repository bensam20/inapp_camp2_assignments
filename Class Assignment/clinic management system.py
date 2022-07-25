# Write a program to build a simple Clinic Management System using Python which
# can perform following operations inside the class CMS
# Admit - This method takes patient details from the user like name,
# gender, age, dob, blood group. A patient_id should be automatically generated
# listPatients - This method displays the details of every patient.
# search - searches for a particular patient using patient_id
# Delete - deletes the record of a particular patient using patient_id
# Update - will ask for the patient_id and other details. It will replace
# the other details with new details.
# Create inherited classes 'OP' and 'NonOP'. 'OP' should have the additional
# Admit function and Non OP a function to generate an OP Ticket with 
# incrementing no for every patient

#defining the CMS class
class CMS:
    patients = {}
    patientID = 100

    #receives the details of patient
    def register(name, gender, age, dob, bldgp):
        CMS.patientID += 1
        CMS.patients[CMS.patientID] = [name, gender, age, dob, bldgp]

    #function to list the patients
    def listPatients():
        print("\nList of Patients:\n")
        for patient in CMS.patients:
            print(patient, CMS.patients[patient])

    #searching patient with patient ID
    def searchPatient(paitent_ID):
        print(CMS.patients[paitent_ID])

    #deleting patient with patient ID
    def deletePatient(patient_ID):
        del CMS.patients[patient_ID]

    #functioin to update the patient details
    def updatePatient(patient_ID,name, gender, age, dob, bldgp):
        CMS.patients[patient_ID] = [name, gender, age, dob, bldgp]

#OP class
class OP(CMS):
    def admit(id,name, gender, age, dob, bldgp,disease,numOfDays):
        CMS.patients[id] = [name, gender, age, dob, bldgp,disease,numOfDays]

#Non OP Class
class NonOP(CMS):
    token = 0

    def getToken():
        NonOP.token+=1
        return NonOP.token

#registering patients
CMS.register('Harry', 'M', 10, '27/03/2012', 'B+')
CMS.register('Alice', 'F', 12, '01/05/2010', 'O+')

CMS.listPatients() #display patients

CMS.searchPatient(101) #search for a patient

CMS.updatePatient(102,'Alice', 'F', 12, '21/07/2010', 'A+') #updating a patient

OP.admit(101,'Harry', 'M', 10, '27/03/2012', 'B+','Fever',2) #admitting an OP patient

CMS.listPatients()

CMS.deletePatient(102) #deleting a patient

CMS.listPatients()

tkn = NonOP.getToken() #getting token for Non OP patient
print(tkn)
