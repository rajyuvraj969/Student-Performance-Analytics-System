# Student Performance Analytics System

## EWB Courses - Python with AI Project

A Python-based data-analysis project that reads student records from a CSV file and performs student performance analysis using **Python, NumPy and Pandas**.

## Project Objective

The objective is to process student marks and attendance data and generate meaningful results such as:

- Total marks
- Average marks
- Grades
- Pass/Fail status
- Highest and lowest performance
- Overall class average
- Subject-wise performance
- Top-performing students
- Attendance analysis

## Technologies Used

- Python
- NumPy
- Pandas
- CSV

## Project Structure

```text
student-performance-analytics/
├── main.py
├── functions.py
├── students.csv
├── student_performance_report.csv
├── README.md
├── Project_Documentation.md
└── requirements.txt
```

## Grading Rule

| Average Marks | Grade |
|---|---|
| 90-100 | A+ |
| 80-89.99 | A |
| 70-79.99 | B |
| 60-69.99 | C |
| 50-59.99 | D |
| Below 50 | F |

## Pass/Fail Rule

A student is marked **PASS** when:

1. Average marks are at least 40, and
2. Marks in every subject are at least 35.

Otherwise the student is marked **FAIL**.

## Subjects

- Python
- Pandas
- NumPy
- Data Analysis

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

The program also creates:

```text
student_performance_report.csv
```

which contains the calculated total, average, grade and status.

## Python Concepts Demonstrated

- Variables
- Data types
- Conditions
- Loops
- Functions
- Pandas DataFrame
- NumPy numerical calculations
- Data analysis

## Submission

Before submission:

- Test the project.
- Create a GitHub repository.
- Upload all project files.
- Add this README.
- Add the project documentation.
- Copy the GitHub repository URL.
- Submit the URL through the EWB Google Form.

**GitHub Repository:** Add your final repository URL here.

## Deadline

15 October 2026
