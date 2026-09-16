totalPointsWon = 0  # Total Number Of Points Won From All The Matches
totalPointsLose = 0
matchWonCount = 0
matchLoseCount = 0
pointsPerMatchWon = 0  # Points Earned For One Match
pointsPerMatchLose = 0
pointsPerSetWon = 0  # Points Earned For One Set
pointsPerSetLose = 0
setsWonPerMatch = 0  # Number Of Sets Won In One Match
setsLosePerMatch = 0
totalSetsWon = 0
totalSetsLose = 0  # Number Of Lost Sets
fiveSetsMatchCount = 0  # Number Of Matches Which Finished In 5 sets (3-2)
threeSetsMatchWonCount = 0  # Number Of Matches Which Fınıshed In 3 sets (3-0)
wonMatchesCount = 0
loseMatchesCount = 0
differenceBiggest = 0  # Number Of The Biggest Point Difference In One Match
totalSetsPlayed = 0
differenceMatch = 0  # Number Of The Match Which Have The Biggest Difference
biggestDifferenceMatch = ""  # TheBiggest Won-Lose Point Difference In One Match

matchCount = int(input("Enter Number Of Matches Your Team Played This Season:"))

for match in range(matchCount):
    maxSetCount = 5
    oppositeName = input(f"\nEnter The Opposite Team's Name In {match+1}.Match:")

    for sets in range(maxSetCount):
        pointsPerSetWon = int(
            input(f"Enter The Points Won In {match+1}.Match and {sets+1}.Set:")
        )
        pointsPerSetLose = int(
            input(f"Enter The Points Lose In {match+1}.Match and {sets+1}.Set:")
        )
        pointsPerMatchWon += pointsPerSetWon
        pointsPerMatchLose += pointsPerSetLose
        totalSetsPlayed += sets + 1

        if pointsPerSetWon > pointsPerSetLose:
            setsWonPerMatch += 1
            totalSetsWon += 1
        else:
            setsLosePerMatch += 1
            totalSetsLose += 1

        if (
            (setsWonPerMatch == 3 and sets == 2)
            or (setsLosePerMatch == 3 and sets == 2)
            or (setsWonPerMatch == 3 and sets == 3)
            or (setsLosePerMatch == 3 and sets == 3)
        ):
            break

    differencePoint = abs(
        pointsPerMatchWon - pointsPerMatchLose
    )  # Point Dıfference In One Match

    if differenceBiggest < differencePoint:
        differenceBiggest = differencePoint
        biggestDifferenceMatch = oppositeName
        differenceMatch = match

    if setsWonPerMatch == 3 and sets == 2:
        threeSetsMatchWonCount += 1
    elif sets == 4:
        fiveSetsMatchCount += 1
    else:
        pass

    if setsWonPerMatch > setsLosePerMatch:
        matchWonCount += 1
    else:
        matchLoseCount += 1

    totalPointsWon += pointsPerMatchWon
    totalPointsLose += pointsPerMatchLose
    avgPointsPerSetWon = pointsPerMatchWon / (sets + 1)
    avgPointsPerSetLose = pointsPerMatchLose / (sets + 1)
    print(
        f"\n+Total Points Won: {pointsPerMatchWon}\n-Total Points Lose: {pointsPerMatchLose}"
    )
    print(f"+Total Sets Won: {setsWonPerMatch}\n-Total Sets Lose: {setsLosePerMatch}")
    print(
        f"+Average Of Points Won Per Set: {avgPointsPerSetWon}\n-Average Of Points Lose Per Set: {avgPointsPerSetLose}"
    )
    pointsPerMatchLose = 0
    pointsPerMatchWon = 0
    setsLosePerMatch = 0
    setsWonPerMatch = 0


avgPointsPerMatchWon = totalPointsWon / matchCount
avgPointsPerMatchLose = totalPointsLose / matchCount
perFiveSetsMatch = fiveSetsMatchCount * 100 / matchCount
perThreeSetsMatchWon = threeSetsMatchWonCount / matchWonCount * 100
print("\n\n\n\n\t\t\t******RESULTS*******\n\n\n\n")
print(
    f"+Total Number Of Points Won: {totalPointsWon}\n-Total Number Of Points Lose: {totalPointsLose}"
)
print(f"\n=Average of Points Won Per Match: {avgPointsPerMatchWon}")
print(
    f"\n+Total Number Of Matches Won: {matchWonCount}\n-Total Number Of Matches Lose: {matchLoseCount}"
)
print(
    f"\n+Number Of Matches Won Without Losing a Set: {threeSetsMatchWonCount}\n+Percentage Of The Matches Without Losing Set To All Matches Won: %{perThreeSetsMatchWon:.2f}"
)
print(
    f"\n=Number Of Matches Finished In 5 Sets: {fiveSetsMatchCount}\n=Percentage Of Matches Finished In 5 Set To All Matches: %{perFiveSetsMatch:.2f}"
)
print(
    f"\nThe Match Which Has Biggest Won-Lose Point Difference Is {differenceMatch}.Match and Name Of The Opposite Team In This Match Is {biggestDifferenceMatch}\nThe Difference Of Points: {differenceBiggest}"
)
