from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes import (
    user_routes, 
    company_routes, 
    business_unit_routes, 
    item_routes, 
    component_routes, 
    subcomponent_routes, 
    auth_routes, 
    admin_routes, 
    utility_routes, 
    order_routes, 
    sensor_data_routes, 
    supplier_price_routes, 
    demand_prediction_routes, 
    inventory_routes, 
    audit_routes, 
    notification_routes
)
from app.db import init_db

app = FastAPI(title="ProSpire SaaS", version="1.0.0")

# Incluir el endpoint de login
app.include_router(auth_routes.router)

# Configuración de CORS
origins = ["http://localhost:3000"]  # Ajusta según sea necesario para el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicialización de la base de datos
@app.on_event("startup")
def startup_event():
    init_db()

# Rutas
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(company_routes.router, prefix="/companies", tags=["Companies"])
app.include_router(business_unit_routes.router, prefix="/business-units", tags=["Business Units"])
app.include_router(item_routes.router, prefix="/items", tags=["Items"])
app.include_router(component_routes.router, prefix="/components", tags=["Components"])
app.include_router(subcomponent_routes.router, prefix="/subcomponents", tags=["Subcomponents"])
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(admin_routes.router, prefix="/admin", tags=["Admin"])
app.include_router(utility_routes.router, prefix="/utilities", tags=["Utilities"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
app.include_router(sensor_data_routes.router, prefix="/sensor-data", tags=["Sensor Data"])
app.include_router(supplier_price_routes.router, prefix="/supplier-prices", tags=["Supplier Prices"])
app.include_router(demand_prediction_routes.router, prefix="/demand-predictions", tags=["Demand Predictions"])
app.include_router(inventory_routes.router, prefix="/inventory", tags=["Inventory"])
app.include_router(audit_routes.router, prefix="/audits", tags=["Audits"])
app.include_router(notification_routes.router, prefix="/notifications", tags=["Notifications"])

@app.get("/")
def read_root():
    return {"message": "Welcome to ProSpire SaaS!"}