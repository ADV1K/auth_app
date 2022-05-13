from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from .. import oauth2
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(prefix="/organisation", tags=["Organisations"])


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.OrgOut)
def create_organization(organisation: schemas.OrgCreate, db: Session = Depends(get_db)):

    # hash the password - organisation.password
    organisation.password = utils.hash(organisation.password)

    new_organisation = models.Organisation(**organisation.dict())
    db.add(new_organisation)
    db.commit()
    db.refresh(new_organisation)

    return new_organisation


@router.get("/users", response_model=List[schemas.UserOut])
def get_users_in_organisation(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    pass
