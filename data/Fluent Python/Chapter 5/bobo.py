
# Example 5-12. Bobo knows that hello requires a persona argument, and retrieves it from the HTTP request

import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person