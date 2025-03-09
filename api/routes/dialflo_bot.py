
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.schema import UserQuery
from api.models import OrderHistory, QueryTypeEnum, Users
from api.database import get_db
from api.utils.query_ai import get_query_ai
import uuid

router = APIRouter()



def add_order_to_db(db: Session, order_type: QueryTypeEnum, user_query: str, username: str, phone: str):
    try:
        # Check if user exist by phone
        user = db.query(Users).filter_by(phone=phone).first()
        
        # NOTE - valodate phone and username before creating user
        if not user and phone is not None :
            user = Users(phone=phone)
            if username:
                user.username = username
            db.add(user)
            db.commit()
            db.refresh(user) 
        
        # Create the new order and assign user_id
        new_order = OrderHistory(
            order_id=str(uuid.uuid4().int)[:6],  
            query=user_query,
            query_type=order_type
        )
        
        if user:
           new_order.user_id = user.id 
        
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return True
    except Exception as e:
        # logger
        db.rollback()  
        print("Error while creating order", str(e))
        return False
    
@router.post('/support-agent')
def ai_support_agent(
        request : UserQuery,
        db: Session = Depends(get_db)
        ):
    """
       API which accepts the order query and username optional and return the Order status accordingly
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