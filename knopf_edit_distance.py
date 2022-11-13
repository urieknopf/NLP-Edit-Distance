# Uriel Knopf - Natural Language processing - ESU - CPSC432

def edit_distance(string_1, string_2):
    # length of string1 = rows, string2 = columns
    length_1, length_2 = (len(string_1) + 1, len(string_2) + 1)
    dist_matrix = [[0 for x in range(length_2)] for x in range(length_1)]
    point_matrix = [[' ' for x in range(length_2)] for x in range(length_1)]

    print("------------------------------------------------")
    print("Words to compare: ", string_1, string_2)

    for row in range(len(string_1)+1):
        for col in range(len(string_2)+1):

            # if first row, cell = col#
            if col == 0:
                dist_matrix[row][col] = row
                if row > 0:
                    point_matrix[row][col] = 'U'

            # if first col, cell = row#
            elif row == 0:
                dist_matrix[row][col] = col
                if col > 0:
                    point_matrix[row][col] = 'L'

            # if letters are same set cost to diag cell
            elif string_1[row - 1] == string_2[col - 1]:
                dist_matrix[row][col] = dist_matrix[row - 1][col - 1]
                point_matrix[row][col] = 'G'

            else:  # if letters are not the same
                dist_matrix[row][col] = min(dist_matrix[row - 1][col] + 1,  # delete
                                            dist_matrix[row][col - 1] + 1,  # insert
                                            dist_matrix[row - 1][col - 1] + 2)  # substitute

                if (dist_matrix[row - 1][col - 1] + 2) == (dist_matrix[row][col]):
                    point_matrix[row][col] = 'G'
                elif ((dist_matrix[row][col - 1] + 1) == (dist_matrix[row][col])) and (
                        (dist_matrix[row][col]) == (dist_matrix[row - 1][col] + 1)):
                    point_matrix[row][col] = 'G'
                elif (dist_matrix[row][col - 1] + 1) == (dist_matrix[row][col]):
                    point_matrix[row][col] = 'L'
                else:
                    point_matrix[row][col] = 'U'

# Print edit dist:
    print("Min edit distance: ", dist_matrix[len(string_1)][len(string_2)])

# prints word
    for col in range(length_2):
        if col == 0:
            print("\n    #  ", end='')
        elif col+1 == length_2:
            print(string_2[col - 1], " ")
        else:
            print(string_2[col - 1], " ", end='')

# prints word + current row distance matrix
    for row in range(length_1):
        if row == 0:
            print("#  ", end='')
        else:
            print(string_1[row - 1], " ", end='')
        print(dist_matrix[row])

    print(" ")

# prints target word
    for col in range(length_2):
        if col == 0:
            print("     #    ", end='')
        elif col+1 == length_2:
            print(string_2[col - 1], " ")
        else:
            print(string_2[col - 1], "   ", end='')

# prints start word letter + current row pointmatrix
    for row in range(length_1):
        if row == 0:
            print("#  ", end='')
        else:
            print(string_1[row - 1], " ", end='')
        print(point_matrix[row])
    print(" ")

# ################## lets code some alignment!! ############
    alignment_list = []
    row_position, col_position = (len(string_1), len(string_2))
    position = point_matrix[row_position][col_position]

    while position != ' ':
        if position == 'G':
            if dist_matrix[row_position][col_position] == dist_matrix[row_position - 1][col_position - 1]:
                # letters same: if value same nothing changes
                alignment_list.append(" ")
            else:
                # if values not same: substitution happened
                alignment_list.append("s")
            # next position move diagonal
            col_position -= 1
            row_position -= 1
        elif position == 'U':
            # next position move up a row
            row_position -= 1
            alignment_list.append("d")
        else:  # position == 'L':
            # next position move over column
            col_position -= 1
            alignment_list.append("i")
        position = point_matrix[row_position][col_position]

    list_length = len(alignment_list)
    list_length_2, list_length_3 = list_length,  list_length
    count_2, count_1 = 0, 0

    # print second input word
    while list_length > 0:
        if alignment_list[list_length - 1] == "i":
            print("*", end="")
        else:
            print(string_1[count_1], end="")
            count_1 += 1
        # end of while loop
        list_length -= 1
    print(" ")

    # print an | for every letter or action in the edit path
    for i in range(list_length_2):
            print("|", end="")
    print(" ")

    # print target word (first input word)
    while list_length_2 > 0:
        if alignment_list[list_length_2 - 1] == "d":
            print("*", end="")
        else:
            print(string_2[count_2], end="")
            count_2 += 1
        # end of while loop
        list_length_2 -= 1
    print(" ")

    # print action letters
    while list_length_3 > 0:
        print(alignment_list[list_length_3 - 1], end="")
        # end of while loop
        list_length_3 -= 1
    print("\n\n")


# ############## Main? #################################
str_2 = input("Enter target string: ")  # string_2
str_1 = input("Enter initial string: ")  # string_1
edit_distance(str_1, str_2)


# words = ["acress", "actress", "cress", "access", "across", "acres"]
# for words2_6 in range(1, 6):
#     edit_distance(words[0], words[words2_6])
# ^^^ input for testing

