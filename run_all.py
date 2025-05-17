import threading
import uvicorn
import streamlit.web.bootstrap as st_bootstrap

def run_fastapi():
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

def run_streamlit():
    st_bootstrap.run("app.py", "", [], {})

if __name__ == "__main__":
    threading.Thread(target=run_fastapi).start()
    run_streamlit()
