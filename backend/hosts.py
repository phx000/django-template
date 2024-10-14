from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'api', 'api.drf.urls', name='api'),
    host(r'ws', 'api.ws.routing', name='ws'),
)
