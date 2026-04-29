import pandas as pd

# CSV file read
df = pd.read_csv("jobs.csv")

print("Full Data:\n")
print(df)

print("\nFirst 5 rows:\n")
print(df.head())
# Skills clean
df['skills'] = df['skills'].str.lower().str.split(',')

# Flatten skills list
all_skills = []
for skills in df['skills']:
    all_skills.extend(skills)

# Skill frequency
skill_freq = pd.Series(all_skills).value_counts()

print("\nTop Skills in Market:\n")
print(skill_freq)
import matplotlib.pyplot as plt

# Top 5 skills graph
skill_freq.head(5).plot(kind='bar')

plt.title("Top Skills Demand")
plt.xlabel("Skills")
plt.ylabel("Count")

plt.show()