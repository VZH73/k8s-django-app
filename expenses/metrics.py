from prometheus_client import Counter, Gauge, Histogram

REQUEST_COUNT = Counter(
    "django_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "http_status"],
)

REQUEST_LATENCY = Histogram(
    "django_request_latency_seconds",
    "Request latency",
    ["endpoint"],
)

EXPENSE_CREATED_EVENTS = Counter(
    "expenses_created_events_total",
    "Expense creation events handled by this pod",
)

EXPENSE_RECORDS_TOTAL = Gauge(
    "expenses_records_total",
    "Current total number of expense records in database",
)

EXPENSE_TOTAL_AMOUNT = Gauge(
    "expenses_total_amount",
    "Current total amount of expenses in database",
)