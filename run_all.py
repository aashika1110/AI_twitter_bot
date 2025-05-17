# run_all.py
import subprocess
import threading

def run_fastapi():
    subprocess.run(["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "app.py"])

# Start FastAPI and Streamlit in parallel threads
if __name__ == "__main__":
    threading.Thread(target=run_fastapi).start()
    threading.Thread(target=run_streamlit).start()

