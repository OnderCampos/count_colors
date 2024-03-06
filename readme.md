# FastAPI Project Setup


## Step 1: Create a Virtual Environment

Open a terminal or command prompt and navigate to the directory where you want to create your FastAPI project. Run the following commands:

```bash
# On Windows
python -m venv venv

# On macOS/Linux
python3 -m venv venv
```

## Step 2: Activate Virtual Environment

```bash
# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

## Step 3: Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
```

## Step 4: Run
```bash
python -m uvicorn src.main:app --reload
```