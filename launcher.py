import multiprocessing
import os

# streamlit側の起動関数
def run_streamlit():
    os.system('streamlit run app.py')

# FastAPI側の起動関数
def run_fastapi():
    os.system('uvicorn sql_app.main:app --host 0.0.0.0 --port 8000')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=run_streamlit)
    p2 = multiprocessing.Process(target=run_fastapi)

    p1.start()
    p2.start()