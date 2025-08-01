import pandas as pd

def project_1_student_grades():
    print("\n PROJECT 1: STUDENT GRADE ANALYZER")
    print("-" * 40)

    students_data ={
        'student_id':['5001','5002','5003','5004','5005','5006','5007','5008'],
        'name':['alice','puni','anu','navya','kavitha','mouni','pujitha','sujatha'],
        'grade':['A','B','C','D','E','A','B','C'],
        'math_score':['88','82','85','72','88','76','70','75'],
        'english_score':['80','78','92','65','90','85','88','70'],
        'science_score':['90','75','88','72','85','92','80','68'],
        'attendance':['95','88','92','85','90','94','87','82']
    }
    df = pd.DataFrame(students_data)
    score_cols = ['math_score', 'english_score', 'science_score', 'attendance']
    df[score_cols] = df[score_cols].astype(int)
    print("your tasks:")
    print("1. calculate total score for each student")
    df['total_score'] = df['math_score'] + df['english_score'] + df['science_score']
    print(df[['name', 'total_score']])

    print("2. find average score by grade")
    avg_by_grade = df.groupby('grade')['total_score'].mean()
    print(avg_by_grade)

    print("\n3.find student with attendance > 90%")
    high_attendance = df[df['attendance'] > 90]
    print(f"students with greater than 90% attendance: {len(high_attendance)}")
    print(high_attendance[['name','attendance']])

    print("\n4.find top 3 students by total score")
    top_students = df.nlargest(3, 'total_score')
    print(top_students[['name', 'total_score']])

    return df

project_1_student_grades()