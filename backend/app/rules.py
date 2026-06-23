from datetime import datetime, time
from app.models import Trade, Strategy


def check_symbol_rule(trade: Trade, strategy: Strategy) -> str | None:
    if trade.symbol not in strategy.allowed_symbols:
        return f"Symbol {trade.symbol} is not allowed in your watchlist."
    return None


def check_time_window_rule(trade: Trade, strategy: Strategy) -> str | None:
    entry_time = trade.entry_time.time()
    start = datetime.strptime(strategy.start_time, "%H:%M").time()
    end = datetime.strptime(strategy.end_time, "%H:%M").time()

    if not (start <= entry_time <= end):
        return (
            f"Entry time {entry_time} is outside your allowed window "
            f"of {strategy.start_time}--{strategy.end_time}."
        )
    
    return None

def check_max_loss_rule(trade: Trade, strategy: Strategy) -> str | None:
    if trade.realized_pnl < -strategy.max_loss_per_trade:
        return (
            f"Loss of ${abs(trade.realized_pnl)} exceeded your max loss "
            f"of ${strategy.max_loss_per_trade}."
        )
    
    return None