
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.schema import UserQuery
from api.models import OrderHistory, QueryTypeEnum
from api.database import get_db
from api.utils.query_ai import get_query_ai
import uuid

router = APIRouter()



def add_order_to_db(db, order_type, user_query, username, phone):
    try:
        new_order = OrderHistory()
        new_order.order_id = str(uuid.uuid4().int)[:6]
        new_order.query = user_query
        new_order.query_type = order_type
        if username is not None:
            print("username", username)
            new_order.customer_name = username
        if phone is not None:
            new_order.customer_phone = phone
        
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return True
    
    except Exception as e:
        # logger
        print("Error while creating order", str(e))
        return False
    
@router.post('/support-agent')
def ai_support_agent(
        request : UserQuery,
        db: Session = Depends(get_db)
        ):
    """
       API which accepts the order query and username optional
    """
    # get the data
    user_query = request.query
    username = request.username
    phone = request.phone
    
    # TODO - Add classfification algo modal here to catrgoried query
    query_type = get_query_ai(request.query)

    if query_type == "order_status":
        # store the order data
        order_type = QueryTypeEnum.ORDER_STATUS
        resp = add_order_to_db(db, order_type, user_query, username, phone)
        if not resp:
            pass
        
        response = "Your order is on the way. It will arrive in 20 minutes."
        
    elif query_type == "new_order":
        order_type = QueryTypeEnum.NEW_ORDER
        resp = add_order_to_db(db, order_type, user_query, username, phone)
        
        if phone is None or username is None:
            response = "Please provide your name and phone number to proceed."
        else:
            response = "Your order is now placed. will keep you posted."
        
    else:
        response = "Sorry, I don't understand your request."
   
    return {"query": request.query, "response": response}