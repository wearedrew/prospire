from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"
    BILLING = "BILLING"
    DEMAND_MANAGER = "DEMAND_MANAGER"