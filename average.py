numberOfScores = 0
score = 0
total = 0
scoreCount = 0
average = 0.0

#Accept the number of scores to average
numberOfScores = input("Please Enter the Number of Scores You Want to Average: ")

#Add a loop to make this code repeat untill scoreount = numberOfScores

score = int(input("Please enter a score: "))
total = total + score
scoreCount = scoreCount + 1


average = total / numberOfScores
print (average)
