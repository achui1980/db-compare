from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    success: bool = Field(default=True)
    code: Optional[str] = None
    msg: str = Field(default="")
    timestamp: str = Field(default=str(datetime.now()))
    data: Any = None
    def success_response(self, data: Any = None):
        self.success = True
        self.code = "200"
        self.msg = "成功"
        self.timestamp = str(datetime.now())
        self.data = data
        return self
    def error_response(self, code: str, msg: str, data: Any = None):
        self.success = False
        self.code = code
        self.msg = msg
        self.timestamp = str(datetime.now())
        self.data
        return self