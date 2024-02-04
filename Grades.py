grades = {'Biology': 80, 'Physics': 88, 'Chemistry': 98, 'Math': 89, 'English': 79,
          'Music': 67, 'History': 68, 'Art': 53, 'Economics': 95, 'Psychology': 88}

def calculate_average_score(subject):
    # Check if the subject exists in the grades dictionary
    if subject in grades:
        # Calculate the sum of scores excluding the given subject
        total = sum([grades[subj] for subj in grades if subj != subject])
        # Calculate the average score excluding the given subject
        average = total / (len(grades) - 1)
        # Print the average score rounded to two decimals
        print(f'{average:.2f}')
    else:
        print("Subject not found in dictionary.")

if __name__ == "__main__":
    import sys

    # Check if an argument (subject) is provided in the command line
    if len(sys.argv) != 2:
        print("Provide a single subject")
    else:
        subject = sys.argv[1]
        calculate_average_score(subject)