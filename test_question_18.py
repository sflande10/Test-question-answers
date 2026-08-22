import pandas as pd

df = pd.read_csv('students_3.csv')

avg = df['score'].mean()
print("Average score:", avg)

best = df.loc[df['score'].idxmax()]
print("Highest scorer:", best['name'], best['score'])

top_students = df[df['score'] >= 70]

top_students.to_json('top_students.json', orient='records', indent=4)

print("Saved", len(top_students), "students to top_students.json")