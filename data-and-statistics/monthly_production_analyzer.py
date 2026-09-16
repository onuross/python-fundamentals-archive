def main():
    try:
        infile = open("mountly_production.txt", "r")
        machineCount = infile.readline()
        productionTotals = [0] * int(machineCount)
        dayCount = [0] * int(machineCount)
        takeProductionData(infile, productionTotals, dayCount)
        infile.close()
        statistics(productionTotals, dayCount, machineCount)
    except IOError:
        print("Could Not Open or Read The File!")


def takeProductionData(infile, productionTotals, dayCount):
    dayNo = infile.readline()
    while dayNo != "":
        machineNo = int(infile.readline())
        dailyProduction = float(infile.readline())
    productionTotals[machineNo - 1] += dailyProduction
    dayCount[machineNo - 1] += 1
    dayNo = infile.readline()


def statistics(productionTotals, dayCount, machineCount):
    print(
        "Machine No   Monthly Production  Number of Production Days   Daily Production"
    )
    print(
        "----------   ------------------  -------------------------   ----------------"
    )
    for machineNo in range(int(machineCount)):
        print(f"{machineNo + 1:.10d}", end="    ")
        print(f"{productionTotals[machineNo]:.18d}", end="   ")
        print(f"{dayCount[machineNo]:.25d}", end="   ")
        if dayCount[machineNo] != 0:
            print(
                productionTotals[machineNo] / dayCount[machineNo]
            )  # daily average production
        else:
            print(0)

    print(sum(productionTotals))
    maxProduction = max(productionTotals)
    maxProductionMachine = productionTotals.index(maxProduction) + 1
    print(maxProductionMachine)
    print(maxProduction)


main()
