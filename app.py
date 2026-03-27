# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello FastApI"}


from fastapi import FastAPI,HTTPException
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/get-csv-data")
def get_csv_data():

    try:
        df = pd.read_csv("students_complete.csv")

        return {
            "columns": list(df.columns),
            "total_rows": len(df),
            "data": df.fillna("").to_dict(orient="records")
        }

    except FileNotFoundError:
        return {
            "error": "students_complete.csv not found. Make sure it is in same folder as app.py"
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    
@app.get("/get-student/{student_id}")
def get_student_by_studentid(student_id: str):

    try:
        df = pd.read_csv("students_complete.csv")

        student = df[df["student_id"] == student_id]

        if student.empty:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student.fillna("").to_dict(orient="records")[0]

    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="CSV file not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )