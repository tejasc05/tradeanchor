from pydantic import BaseModel
from datetime import datetime
from typing import List

class Trade(BaseModel):
    symbol: str
    entry_time: datetime
    exit_time: datetime
    side: str
    quantity: int
    entry_price: float
    exit_price: float
    realized_pnl: float

class Strategy(BaseModel):
    allowed_symbols: List[str]
    start_time: str
    end_time: str
    max_loss_per_trade: float

class TradeEvaluation(BaseModel):
    trade: Trade
    followed_plan: bool
    violations: List[str] 

class EvaluationRequest(BaseModel):
    trades: List[Trade]
    strategy: Strategy