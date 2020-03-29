'''Table Printer: Write a function named printTable()
that takes a list of lists of strings and displays it
in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number
of strings.'''

def printTable(table):

    colWidths = [0] * len(table)

    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]), end = ' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
