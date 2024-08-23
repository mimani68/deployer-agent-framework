import time

recent_requests = {}

def is_request_called_recently(endpoint, payload, cmd, window=300):
    current_time = time.time()

    # Clear out old entries
    for key in list(recent_requests.keys()):
        if current_time - recent_requests[key]['time'] > window:
            del recent_requests[key]

    request_key = (endpoint, cmd, frozenset(payload.items()))
    
    if request_key in recent_requests:
        return True
    
    # Store the new request
    recent_requests[request_key] = {
        'time': current_time,
        'payload': payload
    }
    
    return False