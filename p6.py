# AIM: Implement Naive Bayes Algorithm

from RWP import rwp_examples

total_exp = 12

# Count attribute values
def tot(attribute, value):
    return sum(
        1 for data in rwp_examples.values()
        if data[attribute] == value
    )

# Calculate conditional probability
def getProbab(attribute, attribval, answer):
    count = sum(
        1 for data in rwp_examples.values()
        if data[attribute] == attribval and data['ans'] == answer
    )
    return count / tot('ans', answer)

# Calculate and display probabilities
def main():
    attributes = [
        ('Alt', 'Y', 'Alternate Restaurant: Yes'),
        ('Alt', 'N', 'Alternate Restaurant: No'),
        ('Est', '0-10', 'Estimated Wait: 0-10 minutes'),
        ('Est', '10-30', 'Estimated Wait: 10-30 minutes'),
        ('Est', '30-60', 'Estimated Wait: 30-60 minutes'),
        ('Est', '>60', 'Estimated Wait: More than 60 minutes'),
        ('Pat', 'S', 'Patrons: Some'),
        ('Pat', 'N', 'Patrons: None'),
        ('Pat', 'F', 'Patrons: Full'),
        ('Type', 'T', 'Restaurant Type: Thai')
    ]

    for attribute, value, description in attributes:
        probability = tot(attribute, value) / total_exp

        print(f"\n{description}")

        for answer in ['Y', 'N']:
            result = (
                getProbab(attribute, value, answer)
                * tot('ans', answer) / total_exp
                / probability
            ) * 100

            print(f"Will Wait = {answer}: {result:.2f}%")

main()