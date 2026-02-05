def progress_bar_util(current: int, total: int, size: int = 10) -> str:
  filled = int(size * current / total)
  empty = size - filled
  return "🟢" * filled + "⚪" * empty