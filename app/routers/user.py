from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session

from app import oauth2
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/profile", response_model=schemas.UserOut)
def get_user_profile(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    return user


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password - user.password
    user.password = utils.hash(user.password)

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
