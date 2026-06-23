from typing import List

from app.models import Trade, Strategy, TradeEvaluation
from app.rules import (
    check_symbol_rule,
    check_time_window_rule,
    check_max_loss_rule
)

def evaluate_trade(trade: Trade, strategy: Strategy) -> TradeEvaluation:
    violations = []

    rule_checks = [
        check_symbol_rule,
        check_time_window_rule,
        check_max_loss_rule
    ]

    for rule_check in rule_checks:
        violation = rule_check(trade, strategy)

        if violation is not None:
            violations.append(violation)

    return TradeEvaluation(
        trade=trade,
        followed_plan=len(violations) == 0,
        violations=violations,
    )
    
def evaluate_trades(trades: List[Trade], strategy: Strategy) -> List[TradeEvaluation]:
    return [evaluate_trade(trade, strategy) for trade in trades]