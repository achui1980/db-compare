from datetime import datetime
from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.models import DatabaseConfig, DatabaseConfigUpdate
from app.models import DatabaseConfigCreate

def create_db_config(db: Session, config: DatabaseConfigCreate) -> DatabaseConfig:
    db_config = DatabaseConfig(
        **config.dict(),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_db_configs(db: Session, skip: int = 0, limit: int = 100) -> List[DatabaseConfig]:
    return db.query(DatabaseConfig).offset(skip).limit(limit).all()

def get_db_config(db: Session, config_id: int) -> Optional[DatabaseConfig]:
    return db.query(DatabaseConfig).filter(DatabaseConfig.id == config_id).first()

def update_db_config(
    db: Session, config_id: int, config: DatabaseConfigUpdate
) -> Optional[DatabaseConfig]:
    db_config = get_db_config(db, config_id)
    if db_config:
        for key, value in config.dict(exclude_unset=True).items():
            setattr(db_config, key, value)
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_db_config(db: Session, config_id: int) -> bool:
    db_config = get_db_config(db, config_id)
    if db_config:
        db.delete(db_config)
        db.commit()
        return True
    return False