import logging
import time

logger = logging.getLogger(__name__)


class AccessLogStdoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        duration = time.perf_counter() - start

        remote_addr = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR', '-')
        remote_port = request.META.get('REMOTE_PORT', '-')
        method = request.method
        full_path = request.get_full_path()
        protocol = request.META.get('SERVER_PROTOCOL', 'HTTP/1.1')
        status_code = response.status_code
        content_length = len(response.content) if hasattr(response, 'content') else '-'
        referer = request.META.get('HTTP_REFERER', '-')
        user_agent = request.META.get('HTTP_USER_AGENT', '-')

        logger.info(
            f'{remote_addr}:{remote_port} - "{method} {full_path} {protocol}" {status_code} {content_length} '
            f'"{referer}" "{user_agent}" {duration:.3f}',
        )

        return response
