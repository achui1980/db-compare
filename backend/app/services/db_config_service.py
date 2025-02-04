from datetime import datetime
import logging
from typing import List, Optional
from uuid import UUID
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.domain.db_config import DatabaseConfig, DatabaseConfigUpdate, DatabaseConfigCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
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

def test_db_connection(config: DatabaseConfig) -> bool:
    engine = create_engine(config.connection_string)
    connection = engine.connect()
    connection.close()
    return True
