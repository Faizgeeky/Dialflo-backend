order_status_keywords = {"where", "order", "my", "track", "status"}
new_order_keywords = {"place", "new", "order", "buy", "purchase"}


def get_query_ai(query: str):
    words = set(query.lower().split())  
    
    order_status_count = len(words & order_status_keywords)
    new_order_count = len(words & new_order_keywords)

    if order_status_count > new_order_count:
        return "order_status"
    elif new_order_count > order_status_count:
        return "new_order"
    elif order_status_count == new_order_count and order_status_count > 0:
        return "ambiguous"  
    else:
        return "unknown"

