# Experiment 10: Data Cleaning and Visualization

## Aim

To clean and analyze student data using Pandas and NumPy, handle missing marks, classify students as Pass or Fail, and visualize the relationship and distribution of study hours and marks using Matplotlib.

## Algorithm

1. Import Pandas, NumPy, and `matplotlib.pyplot`.
2. Load the student dataset into a Pandas DataFrame (or create a DataFrame containing student names, marks, and study hours).
3. Display the original student data.
4. Check the `Marks` column for missing values.
5. Replace missing marks with the mean of the available marks.
6. Use NumPy to add a `Grade` column: assign `Pass` when marks are at least 75; otherwise assign `Fail`.
7. Display the cleaned DataFrame, including the calculated grades.
8. Create a bar chart comparing each student's study hours and marks.
9. Create a line chart showing the relationship between study hours and marks.
10. Create a pie chart showing each student's share of the study hours.
11. Create a histogram showing the distribution of marks.
12. Create a scatter plot of study hours against marks.
13. Add suitable labels and titles to the charts, then display each chart using `plt.show()`.
