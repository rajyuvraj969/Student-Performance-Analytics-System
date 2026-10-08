"""
Student Performance Analytics System
EWB Courses | Python with AI

Technology:
- Python
- NumPy
- Pandas

This project follows the assignment requirements:
dataset -> Pandas DataFrame -> NumPy calculations ->
functions/loops/conditions -> analysis -> readable output.
"""

import numpy as np
import pandas as pd

from functions import SUBJECTS, build_analysis, get_top_performers, subject_wise_analysis


DATA_FILE = "students.csv"


def display_header(title: str) -> None:
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def main() -> None:
    # Step 1 & 2: Load and organize data using Pandas.
    df = pd.read_csv(DATA_FILE)

    display_header("STUDENT PERFORMANCE ANALYTICS SYSTEM")

    print("\n--- DATASET OVERVIEW ---")
    print(f"Number of students : {len(df)}")
    print(f"Number of subjects : {len(SUBJECTS)}")
    print(f"Columns            : {', '.join(df.columns)}")

    print("\n--- FIRST 5 RECORDS ---")
    print(df.head().to_string(index=False))

    print("\n--- DATA INFORMATION ---")
    df.info()

    # Step 3: Process data using functions, NumPy, loops and conditions.
    result = build_analysis(df)

    print("\n--- PROCESSED STUDENT PERFORMANCE ---")
    display_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Status"
    ]
    print(result[display_columns].to_string(index=False))

    # Step 4: Perform analysis.
    subject_avg = subject_wise_analysis(result)

    top_student = result.loc[result["Average_Marks"].idxmax()]
    lowest_student = result.loc[result["Average_Marks"].idxmin()]

    class_average = np.round(result["Average_Marks"].mean(), 2)
    highest_average = np.round(result["Average_Marks"].max(), 2)
    lowest_average = np.round(result["Average_Marks"].min(), 2)

    pass_count = int((result["Status"] == "PASS").sum())
    fail_count = int((result["Status"] == "FAIL").sum())

    best_subject = subject_avg.idxmax()
    lowest_subject = subject_avg.idxmin()

    print("\n--- CLASS PERFORMANCE SUMMARY ---")
    print(f"Overall class average : {class_average}")
    print(f"Highest average       : {highest_average}")
    print(f"Lowest average        : {lowest_average}")
    print(f"Students passed       : {pass_count}")
    print(f"Students failed       : {fail_count}")

    print("\n--- TOP PERFORMER ---")
    print(f"Student ID : {top_student['Student_ID']}")
    print(f"Name       : {top_student['Name']}")
    print(f"Department : {top_student['Department']}")
    print(f"Average    : {top_student['Average_Marks']}")
    print(f"Grade      : {top_student['Grade']}")

    print("\n--- LOWEST PERFORMER ---")
    print(f"Student ID : {lowest_student['Student_ID']}")
    print(f"Name       : {lowest_student['Name']}")
    print(f"Average    : {lowest_student['Average_Marks']}")
    print(f"Grade      : {lowest_student['Grade']}")

    print("\n--- SUBJECT-WISE PERFORMANCE ---")
    for subject, average in subject_avg.items():
        print(f"{subject.replace('_', ' '):15}: {average}")

    print(f"\nBest subject    : {best_subject.replace('_', ' ')}")
    print(f"Lowest subject  : {lowest_subject.replace('_', ' ')}")

    print("\n--- TOP 3 PERFORMERS ---")
    print(get_top_performers(result, 3).to_string(index=False))

    # Attendance analysis is included because the assignment asks for attendance
    # as part of the student dataset.
    print("\n--- ATTENDANCE ANALYSIS ---")
    attendance_avg = np.round(df["Attendance"].mean(), 2)
    low_attendance_count = int((df["Attendance"] < 75).sum())
    print(f"Average attendance       : {attendance_avg}%")
    print(f"Students below 75%       : {low_attendance_count}")

    # Save the final processed dataset for easy inspection.
    output_file = "student_performance_report.csv"
    result.to_csv(output_file, index=False)

    print("\n--- FINAL OUTPUT ---")
    print(f"Processed report saved as: {output_file}")
    print("Project analysis completed successfully.")


if __name__ == "__main__":
    main()
