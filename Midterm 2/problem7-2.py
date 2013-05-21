import random
import pylab

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

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the mean score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    scores = []
    
    for t in range(numTrials):
        m1Exam = Midterm1Score()
        m2Exam = Midterm2Score()
        finalExam = FinalExamScore()
        finalScore = calculateFinalScore(m1Exam, m2Exam, finalExam)
        scores.append(finalScore)
    return scores


def plotQuizzes():
#  Please only use the following Pylab functions:
# show, plot, title, xlabel, ylabel, legend, figure, and hist.

    scores = []
    scores = generateScores(10000)

    pylab.hist(scores, range = (55,90), bins = 7)
#    pylab.hist(range(2500), scores)
    pylab.title('Distribution of Scores')    
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.legend()
    #pylab.figure()
    pylab.show()

plotQuizzes()
