import pandas as pd 

def main():
    students = pd.read_csv("attendance.csv")
    val = students.sample(1)['student'].values[0]
    print("SELECTED STUDENT = {}".format(val))

if __name__ == "__main__":
    main()
