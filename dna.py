import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: dna.py filename.csv filename.txt")
        return

    # TODO: Read database file into a variable
    database = []
    database_file = open(sys.argv[1])
    database_reader = csv.DictReader(database_file)
    for i in database_reader:
        database.append(i)

    # TODO: Read DNA sequence file into a variable
    sequence_file = open(sys.argv[2], "r")
    sequence_reader = sequence_file.read()

    len_k = len(database[0].keys()) - 1

    len_d = len(database)
    # TODO: Find longest match of each STR in DNA sequence

    str_sequence = []
    for i in range(len_k):
        str_sequence.append(longest_match(sequence_reader, list(database[i])[i + 1]))

    list_c = []
    for i in range(len_d):
        list_b = (list(database[i].values()))
        del list_b[0]
        for j in range(len(list_b)):
            list_b[j] = (int(list_b[j]))
        list_c.append(list_b)

    # TODO: Check database for matching profiles
    for i in range(len(list_c)):
        if list_c[i] == str_sequence:
            print(list(database[i].values())[0])
        elif str_sequence not in list_c:
            print("No match")
            return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
