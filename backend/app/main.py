from fastapi import FastAPI, UploadFile, File
from app.csv_parser import parse_trades_csv
import tempfile
import os
from app.models import EvaluationRequest
from app.evaluator import evaluate_trades
from app.statistics import calculate_statistics


# creating and naming the api
app = FastAPI(title="TradeAnchor API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/evaluate")
def evaluate(req: EvaluationRequest):
    evaluations = evaluate_trades(req.trades, req.strategy)
    
    summary = calculate_statistics(evaluations)

    return {
        **summary,
        "evaluations": evaluations
    }

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        contents = await file.read()
        temp_file.write(contents)
        temp_path = temp_file.name

    try:
        trades = parse_trades_csv(temp_path)

        return {
            "message": "CSV parsed successfully.",
            "num_trades": len(trades),
            "trades": trades,
        }
    

    finally:
        os.remove(temp_path)


