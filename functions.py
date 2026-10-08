"""
Reusable functions for the Student Performance Analytics System.
Project requirement basis: Python, functions, loops, conditions, NumPy and Pandas.
"""

import numpy as np
import pandas as pd


SUBJECTS = ["Python", "Pandas", "NumPy", "Data_Analysis"]


def calculate_total_and_average(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total and average marks for every student using NumPy."""
    result = df.copy()
    marks = result[SUBJECTS].to_numpy(dtype=float)

    result["Total_Marks"] = np.sum(marks, axis=1)
    result["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)
    return result


def assign_grade(average: float) -> str:
    """Assign a grade using the project's clearly defined grading rule."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_grades(df: pd.DataFrame) -> pd.DataFrame:
    """Add grades using a reusable function."""
    result = df.copy()
    result["Grade"] = result["Average_Marks"].apply(assign_grade)
    return result


def is_pass(row: pd.Series) -> bool:
    """
    Pass rule:
    - Average marks must be at least 40.
    - Marks in every subject must be at least 35.
    """
    return row["Average_Marks"] >= 40 and all(
        row[subject] >= 35 for subject in SUBJECTS
    )


def add_pass_fail(df: pd.DataFrame) -> pd.DataFrame:
    """Add Pass/Fail status using a loop through DataFrame rows."""
    result = df.copy()
    statuses = []

    for _, row in result.iterrows():
        statuses.append("PASS" if is_pass(row) else "FAIL")

    result["Status"] = statuses
    return result


def subject_wise_analysis(df: pd.DataFrame) -> pd.Series:
    """Return average marks for each subject."""
    return np.round(df[SUBJECTS].mean(), 2)


def get_top_performers(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Return the top n students by average marks."""
    return df.nlargest(n, "Average_Marks")[
        ["Student_ID", "Name", "Department", "Average_Marks", "Grade", "Status"]
    ]


def build_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Run the main processing pipeline."""
    result = calculate_total_and_average(df)
    result = add_grades(result)
    result = add_pass_fail(result)
    return result
