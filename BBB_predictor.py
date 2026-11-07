import pandas as pd 
import numpy as np 

brain_drugs = {
    "Name" : ["Drug_A", "Drug_B", "Drug_C", "Drug_D", "Drug_E", "Drug_F"],
    "Molecular_Weight" : [320, 480, 210, 550, 380, 290],
    "Solubility" : [0.7, 0.2, 0.9, 0.6, 0.4, 0.8],
    "Toxicity" : [0.1, 0.3, 0.05, 0.15, 0.25, 0.08],
    "Activity" : [0.8, 0.6, 0.9, 0.7, 0.4, 0.75]
}

df1 = pd.DataFrame(brain_drugs)

new_drug = {
    "Name" : "Drug_H",
    "Molecular_Weight" : 490,
    "Solubility" : 0.3,
    "Toxicity" : 0.7,
    "Activity" : 0.85
}
df2 = pd.DataFrame([new_drug])
df = pd.concat([df1, df2], ignore_index=True)

df["MW_Pass"] = df["Molecular_Weight"] < 450
df["Sol_Pass"] = df["Solubility"] > 0.3
df["Tox_Pass"] = df["Toxicity"] < 0.2
df["Act_Pass"] = df["Activity"] > 0.5

df["Rule_passed"] = (df["MW_Pass"].astype(int) + df["Sol_Pass"].astype(int) + df["Tox_Pass"].astype(int) + df["Act_Pass"].astype(int))

df["MW_Pass"] = np.where(df["Molecular_Weight"] < 450, "Pass", "Fail")
df["Sol_Pass"] = np.where(df["Solubility"] > 0.3, "Pass", "Fail")
df["Tox_Pass"] = np.where(df["Toxicity"] < 0.2, "Pass", "Fail")
df["Act_Pass"] = np.where(df["Activity"] > 0.5, "Pass", "Fail")

conditions = [df["Rule_passed"] == 4,
             df["Rule_passed"] == 3
]
evaluation = ["Can cross BBB", "Possibly crosses BBB"]
df["classification"] = np.select(conditions, evaluation, default="Cannot cross BBB")
df.to_csv("BBB_drug_evaluation.csv", index=False)
print("\nDrugs that can cross BBB:\n")
dataframe = (df[df["classification"] == "Can cross BBB"][["Name","Toxicity","Activity"]])
print(dataframe)
dataframe.to_csv("BBB_drugs_summary.csv", index=False)
