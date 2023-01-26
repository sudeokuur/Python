from functools import reduce

def calculate_insulin(blood_glucose, unit_per_mgdl):
    return (blood_glucose - 120) / unit_per_mgdl

def calculate(patients, total_insulin):
    unit_per_mgdl = 1800/total_insulin
    insulin_needed = []
    for p in patients:
        i_n = round(calculate_insulin(p, unit_per_mgdl), 2)
        insulin_needed.append(i_n)
    return insulin_needed

def filter_patients(patients):
    return list(filter(lambda a: a>120, patients))

ctr = 0
glucose_level = {}
insulin_count = {}
pnum = int(input("Enter the number of patients: "))
while ctr < pnum:
    patient_name = input('Enter patient name: ')
    patient_glucose_level = input("Enter patient's 12-hour blood glucose values: ").split()
    patient_glucose_level = list(map(int, patient_glucose_level))
    glucose_level[patient_name] = patient_glucose_level
    filtered_patients = filter_patients(patient_glucose_level)
    print('Glucose values over 120mg/dl: ', filtered_patients)
    patient_insulin_count = int(input("How many times did you take insulin in 12 hours? : "))
    insulinectr = input("Enter insulin doses: ").split()
    if patient_insulin_count != len(insulinectr):
        print("You've entered wrong number of insulin. Please try again.")
    insulinectr = list(map(int, insulinectr))
    insulin_count[patient_name] = reduce(lambda a, b: a+b, insulinectr)
    print("12-hour blood glucose values of patients in service: ")
    print(glucose_level, '\n')
    ctr = ctr + 1

for key, item in glucose_level.items():
    print(f'{key} should take')
    filtered_patients = filter_patients(item)
    insulin_to_be_taken = calculate(filtered_patients, insulin_count[key])
    for index, insuline in enumerate(insulin_to_be_taken):
        print(f'{insuline} unit insulin for {filtered_patients[index]} mg/dl')
    print()
