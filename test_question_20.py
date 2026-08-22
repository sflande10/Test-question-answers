import pandas as pd

df = pd.read_csv('students.csv')

print("First 5 records:")
print(df.head())

avg_score = df['score'].mean()
print(f"\nAverage score: {avg_score:.2f}")

above_70 = df[df['score'] > 70]
print("\nStudents scoring above 70:")
print(above_70)

sorted_df = df.sort_values(by='score', ascending=False)
print("\nStudents sorted by score:")
print(sorted_df)