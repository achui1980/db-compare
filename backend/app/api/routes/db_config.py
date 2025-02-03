from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.services import db_config_service as database_config
from app.domain.db_config import (
    DatabaseConfig,
    DatabaseConfigCreate,
    DatabaseConfigUpdate,
)

from app.services.db_config_service import test_db_connection

router = APIRouter(prefix="/db_configs", tags=["db_configs"])

@router.post("/", response_model=DatabaseConfig)
def create_database_config(
    config: DatabaseConfigCreate,
    db: Session = Depends(get_db)
):
    config = DatabaseConfigCreate(**config.dict())
    return database_config.create_db_config(db=db, config=config)

@router.get("/", response_model=List[DatabaseConfig])
def list_database_configs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return database_config.get_db_configs(db, skip=skip, limit=limit)

@router.get("/{config_id}", response_model=DatabaseConfig)
def get_database_config(
    config_id: int,
    db: Session = Depends(get_db)
):
    db_config = database_config.get_db_config(db, config_id)
    if db_config is None:
        raise HTTPException(status_code=404, detail="数据库配置不存在")
    return db_config

@router.put("/{config_id}", response_model=DatabaseConfig)
def update_database_config(
    config_id: int,
    config: DatabaseConfigUpdate,
    db: Session = Depends(get_db)
):
    db_config = database_config.update_db_config(db, config_id, config)
    if db_config is None:
        raise HTTPException(status_code=404, detail="数据库配置不存在")
    return db_config

@router.delete("/{config_id}")
def delete_database_config(
    config_id: int,
    db: Session = Depends(get_db)
):
    success = database_config.delete_db_config(db, config_id)
    if not success:
        raise HTTPException(status_code=404, detail="数据库配置不存在")
    return {"detail": "删除成功"}

@router.post("/test-connection", response_model=bool)
def test_database_connection_route(
    config: DatabaseConfigCreate
):
    """
    测试数据库连接是否成功
    """
    try:
        success = test_db_connection(config)
        return success
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))