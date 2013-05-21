"""
Midterm 1: 50 <= grade <= 80

Midterm 2: 60 <= grade <= 90

Final Exam: 55 <= grade <= 95

"""

def Midterm1Score():
    return random.choice([x for x in range(50, 81)])

def Midterm2Score():
    return random.choice([x for x in range(60, 91)])

def FinalExamScore():
    return random.choice([x for x in range(55, 96)])


def calculateFinalScore(mid1, mid2, final):
    # takes in midterm1, midterm2, final scores
    mid1 *= .25
    mid2 *= .25
    final *= .50
    total = mid1 + mid2 + final
    return total

def sampleQuizzes():
    """
    Write a Monte Carlo simulation that estimates
    the probability of a student having a final score >= 70 and <= 75. 
    Assume that 10,000 trials are sufficient to provide an accurate answer.
    """
    numTrials = 10000
    m1Exam = 0
    m2Exam = 0
    finalExam = 0
    finalScore = 0

    score70to75 = 0

    for t in range(numTrials):
        m1Exam = Midterm1Score()
        m2Exam = Midterm2Score()
        finalExam = FinalExamScore()
        finalScore = calculateFinalScore(m1Exam, m2Exam, finalExam)
        if finalScore >= 70 and finalScore <= 75:
            score70to75 += 1

    probability70to75 = 0
    probability70to75 = score70to75 * 1.0 / numTrials
    return probability70to75



