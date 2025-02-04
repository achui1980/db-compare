from datetime import datetime
from sqlmodel import Field, SQLModel


class DatabaseConfigBase(SQLModel):
    name: str = Field(..., min_length=1, max_length=100)
    type: str = Field(..., min_length=1, max_length=50)
    host: str
    port: int = Field(default=3306, ge=1, le=65535)
    database: str
    username: str
    password: str
    charset: str = Field(default="utf8mb4")
    is_active: bool = True

    @property
    def connection_string(self) -> str:
        db_type = self.type.lower()
        if db_type == "mysql":
            return f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}?charset={self.charset}"
        elif db_type == "postgresql":
            return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif db_type == "sqlite":
            return f"sqlite:///{self.database}"
        else:
            raise ValueError(f"Unsupported database type: {self.type}")


class DatabaseConfigCreate(DatabaseConfigBase):
    pass


class DatabaseConfigUpdate(DatabaseConfigBase):
    pass


class DatabaseConfig(DatabaseConfigBase, table=True):
    __tablename__ = "database_configs"
    id: int = Field(default=None, primary_key=True, index=True)
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True