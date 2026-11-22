# Experiment 10: Data Cleaning and Visualization

## Aim

To perform data cleaning and analysis on a student dataset using NumPy and Pandas, and to visualize the results using Matplotlib.

## Algorithm

1. Import the required libraries: `pandas`, `numpy`, and `matplotlib.pyplot`.
2. Read the student dataset and create a DataFrame.
3. Display the original dataset.
4. Identify and handle missing values:
   - Check for missing values in the DataFrame.
   - Replace missing values in the `Marks` column with the column mean.
5. Create a new column named `Grade`:
   - Assign `Pass` when marks are greater than or equal to 75.
   - Assign `Fail` otherwise.
6. Display the cleaned and processed DataFrame.
7. Generate a bar chart of study hours against marks.
8. Generate a line chart showing the relationship between study hours and marks.
9. Generate a pie chart representing study hours for each student.
10. Generate a histogram to show the distribution of marks.
11. Generate a scatter plot to analyze the relationship between study hours and marks.
12. Display all charts using `plt.show()`.
