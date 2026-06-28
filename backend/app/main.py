from fastapi import FastAPI
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
       **summary
        "evaluations": evaluations,
    }




