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
    
    total_trades = len(evaluations)
    followed_count = sum(1 for evaluation in evaluations if evaluation.followed_plan)

    if total_trades == 0:
        anchor_score = 0
    else:
        anchor_score=round((followed_count/total_trades)*100, 2)

    in_strategy_pnl = sum(
        evaluation.trade.realized_pnl
        for evaluation in evaluations
        if evaluation.followed_plan
    )

    out_of_strategy_pnl = sum(
        evaluation.trade.realized_pnl
        for evaluation in evaluations
        if not evaluation.followed_plan
    )

    return {
       **summary
        "evaluations": evaluations,
    }




