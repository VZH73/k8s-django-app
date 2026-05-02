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

EXPENSE_CREATED = Counter(
    "expenses_created_total",
    "Number of expenses created",
)

EXPENSE_TOTAL_AMOUNT = Gauge(
    "expenses_total_amount",
    "Total amount of expenses",
)