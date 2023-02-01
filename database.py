def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 52))
    print(db)
    add_test_to_patient(db, 4, "HDL", 120)
    room_numbers = ["103", "232", "333"]
    print("Get patient Ann")
    mrn_to_find = 4
    found_patient = get_patient_entry(db, mrn_to_find)
    if found_patient is False:
        print("Patient mrn {} not found".format(mrn_to_find))
    else:
        print(found_patient)
    print_directory(db, room_numbers)

def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
    for patient, rn in zip(db, room_numbers):
        print("Patient {} is in room {}".format(patient[0], rn))

def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient == False:
        print("Bad entry")
    else:
        patient[3].append([test_name, test_value])


if __name__ == "__main__":
    main_driver()