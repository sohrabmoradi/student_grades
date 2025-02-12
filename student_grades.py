import pandas as pd

# Read the CSV file
df = pd.read_csv("Grades_Short.csv")

# Calculate the final grade as the average of all numerical columns (excluding ID and Name)
df["Final_Grade"] = df.iloc[:, 2:].mean(axis=1)

# Function to determine letter grade
def get_letter_grade(final_grade):
    if final_grade > 90:
        return "A+"
    elif final_grade > 80:
        return "A"
    elif final_grade > 70:
        return "B"
    elif final_grade > 60:
        return "C"
    elif final_grade > 55:
        return "D"
    else:
        return "F"

# Apply function to generate Letter_Grade column
df["Letter_Grade"] = df["Final_Grade"].apply(get_letter_grade)

# Save the modified DataFrame to a new CSV file
df.to_csv("Grades_Modified.csv", index=False)

# Display the first few rows of the modified DataFrame
print(df.head())

