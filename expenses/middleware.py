import time

from .metrics import REQUEST_COUNT, REQUEST_LATENCY


class PrometheusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        latency = time.time() - start_time

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.path,
            http_status=str(response.status_code),
        ).inc()

        REQUEST_LATENCY.labels(endpoint=request.path).observe(latency)

        return response