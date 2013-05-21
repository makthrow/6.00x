correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_sudoku(sqList):
    n = 0
    n = len(sqList)
    checkRow = []
    checkCol = []

    for i in range(n):
        checkRow.append(i + 1)
    for i in range(n):
        checkCol.append(list(checkRow))

    print "checkRow: %r" % checkRow
    print "checkCol: %r" % checkCol

    list_counter = 0

    for l in sqList:
        # two checks.
        # 1. check row matches checkRow
        # 2. check column matches checkList (make list of column lists)
        checkCopyListCol = checkCol[:]
        checkCopyRow = checkRow[:]

        column = 0
        print "checking list %r: %r" % (list_counter, l)
        print "checkCopyListCol, : %r" % (checkCopyListCol)

        for i in l:

            try:
                print "checkCopyRow: %r" % checkCopyRow
                checkCopyRow.remove(i)
            except ValueError:
                print "%r not removed from: %r" % (i, checkCopyRow)
                return False
            print "checkCopyRow: %r" % checkCopyRow
            print "checkCopyListCol-Full: %r" % (checkCopyListCol)

            try:
                print "checkCopyListCol %r: %r" % (column,checkCopyListCol[column])
                checkCopyListCol[column].remove(i)
            except ValueError:
                print "%r not removed from: %r" % (i, checkCopyListCol[column])
                return False

            print "checkCopyRow: %r" % checkCopyRow
            print "checkCopyListCol %r, : %r" % (column, checkCopyListCol[column])
            print "checkCopyListCol-Full: %r" % (checkCopyListCol)
            print "-" * 20
            column += 1
        list_counter +=1
    return True



print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False

