from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
import os
import uuid
from datetime import date

app = FastAPI(
    title="EduDesk IT Agent API",
    description="Charter school IT helpdesk API for device lookups, staff account status, and ticket management.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(__file__)

def load_data(filename):
    with open(os.path.join(BASE_DIR, "mock_data", filename)) as f:
        return json.load(f)

def save_data(filename, data):
    with open(os.path.join(BASE_DIR, "mock_data", filename), "w") as f:
        json.dump(data, f, indent=2)

@app.get("/")
def root():
    return {"message": "EduDesk IT Agent API is running"}

@app.get("/devices")
def get_devices(
    serial: Optional[str] = Query(None, description="Device serial number"),
    assigned_to: Optional[str] = Query(None, description="Staff member name or email")
):
    devices = load_data("devices.json")
    if serial:
        devices = [d for d in devices if serial.lower() in d["serial"].lower()]
    if assigned_to:
        devices = [d for d in devices if assigned_to.lower() in d["assigned_to"].lower()]
    if not devices:
        raise HTTPException(status_code=404, detail="No devices found")
    return devices

@app.get("/users")
def get_users(
    name: Optional[str] = Query(None, description="Staff member display name"),
    email: Optional[str] = Query(None, description="Staff member email address")
):
    users = load_data("staff.json")
    if name:
        users = [u for u in users if name.lower() in u["display_name"].lower()]
    if email:
        users = [u for u in users if email.lower() in u["email"].lower()]
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

@app.get("/tickets")
def get_tickets(
    status: Optional[str] = Query(None, description="Filter by ticket status"),
    staff_name: Optional[str] = Query(None, description="Filter by staff name")
):
    tickets = load_data("tickets.json")
    if status:
        tickets = [t for t in tickets if t["status"].lower() == status.lower()]
    if staff_name:
        tickets = [t for t in tickets if staff_name.lower() in t["staff_name"].lower()]
    return tickets

@app.post("/tickets", status_code=201)
def create_ticket(ticket: dict):
    required = ["staff_name", "issue_category", "description"]
    for field in required:
        if field not in ticket:
            raise HTTPException(status_code=400, detail=f"Missing required field: {field}")

    tickets = load_data("tickets.json")
    new_ticket = {
        "ticket_id": f"TKT-{str(len(tickets) + 1).zfill(3)}",
        "staff_name": ticket["staff_name"],
        "issue_category": ticket["issue_category"],
        "description": ticket["description"],
        "status": "Open",
        "created_date": str(date.today()),
        "assigned_to": "IT Team"
    }
    tickets.append(new_ticket)
    save_data("tickets.json", tickets)
    return new_ticket
