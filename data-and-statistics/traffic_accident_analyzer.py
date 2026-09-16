ACCIDENT_CAUSE_COUNT=10

def get_accident_data_and_generate_lists(accident_file,all_provinces_accident_counts,all_provinces_damage_amount_totals):
    province_code_str=accident_file.readline()
    while province_code_str!="":
        province_code=int(province_code_str)
        accident_cause_code=int(accident_file.readline())
        damage_amount=int(accident_file.readline())
        # update accident_counts and damage_amount_totals lists according to accident data read
        all_provinces_accident_counts[province_code-1][accident_cause_code-1] += 1
        all_provinces_damage_amount_totals[province_code-1][accident_cause_code-1] += damage_amount
        province_code_str=accident_file.readline()

def display_table(two_dimensional_list):
    accident_causes = ["Overspeed", "Rule Violation", "Carelessness", "Inc. Overtaking", "Insomnia",
                        "Awkwardness", "Alcohol", "Close Follow-up", "Aggressiveness", "Other"]
    print("Prov. Code ",end="")
    for accident_cause in accident_causes:
        print(f"{accident_cause:16}",end="")
    print("Total")
    print("---------- ",end="")
    for k in range(ACCIDENT_CAUSE_COUNT):
        print("--------------- ",end="")
    print("-----")
    # print the matrix and also the row and column totals of this matrix
    columnTotal =  [0] * ACCIDENT_CAUSE_COUNT
    for provinceCode in range(81):
        print(f"{provinceCode+1:10}", end="")
        for accidentCauseCode in range(ACCIDENT_CAUSE_COUNT):
            print(f"{two_dimensional_list[provinceCode][accidentCauseCode]:16}", end = "")
        print(f"{sum(two_dimensional_list[provinceCode]):6}")
        print("Total      ",end="")





def main():
    try:
        accident_file=open("traffic_accidents.txt","r")
        # create 2 two-dimensional lists for the total number of accidents and total damage amounts by provinces and accident causes
        allProvincesAccidentCounts = []
        allProvincesDamageAmountTotals = []
        for provinceCode in range(81):
            aProvinceAccidentCounts= [0]*ACCIDENT_CAUSE_COUNT
            allProvincesAccidentCounts.append(aProvinceAccidentCounts)
            aProvinceDamageAmountTotals = [0]*ACCIDENT_CAUSE_COUNT
            allProvincesDamageAmountTotals.append(aProvinceDamageAmountTotals)
        
        # call the corresponding function to get accident data from file and generate lists
        get_accident_data_and_generate_lists(accident_file, allProvincesAccidentCounts, allProvincesDamageAmountTotals)
        accident_file.close()
    except IOError:
        print("Could not open or read data file!")
    else:
        print("Total Number of Accidents in a Year by Provinces and Causes of Accidents")
        # call the corresponding function to display the accident counts table
        display_table(allProvincesAccidentCounts)
        bir_tus=input("press any key and enter to continue...")
        print("Total Damage Amounts in a Year by Provinces and Causes of Accidents")
        # call the corresponding function to display the damage amounts table
        display_table(allProvincesDamageAmountTotals)

main()
