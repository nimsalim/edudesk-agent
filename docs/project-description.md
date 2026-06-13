# EduDesk — Submission Project Description

## Short description (1-2 sentences)
EduDesk is a Microsoft 365 Copilot declarative agent that acts as an IT helpdesk assistant for charter schools, letting staff look up user accounts, devices, and support tickets — and file new tickets — entirely through natural-language chat.

## Problem
Small charter schools run lean IT teams, often a single admin supporting hundreds of staff and devices, with no dedicated helpdesk software. When a teacher's Chromebook won't connect or an account gets disabled, the IT person has to manually dig through spreadsheets or device-management consoles to check account status, device assignment, and whether a ticket already exists — all before they can even start troubleshooting. That triage overhead adds up fast across dozens of daily requests.

## Solution
EduDesk brings that triage workflow directly into Microsoft 365 Copilot, which staff already use every day. It's a declarative agent backed by a custom AI Plugin (OpenAPI v2.4) that exposes four actions to a FastAPI backend:

- **getUsers** — look up a staff member's account status, license, department, and last login
- **getDevices** — look up a device (Chromebook/laptop) by serial number, status, and assignment
- **getTickets** — look up existing IT tickets by ID or status (open or resolved)
- **createTicket** — file a new IT ticket on a staff member's behalf, with category and assignment

Each action returns a custom Adaptive Card, so results render as structured, readable cards inside the Copilot chat rather than raw JSON or plain text.

## How it works
1. A staff member or IT admin asks Copilot a question in plain English (e.g., "Get user Sarah Johnson" or "Submit a ticket for Marcus Williams — his account is disabled and he can't log into Google Classroom for PE class").
2. The declarative agent's AI Plugin matches the request to one of the four OpenAPI actions defined in `ai-plugin.json` / `openapi.yaml`.
3. The action calls the FastAPI MCP server (exposed via a dev tunnel), which reads/writes mock IT data (users, devices, tickets).
4. The response is rendered back into the chat using a static Adaptive Card template bound to that action — giving the staff member a clean card with the account, device, or ticket details, or a confirmation that a new ticket was created.

## Demo walkthrough
The demo video shows a realistic triage flow: a teacher's account is checked first (active, licensed, recent login — so the account is fine), then her assigned Chromebook is checked (active, properly assigned — so the device is fine), then an existing ticket for that exact WiFi issue is found (avoiding a duplicate), and finally a brand-new ticket is filed for a different staff member's disabled-account issue — all without leaving Copilot or touching a separate ticketing portal.

## Technologies used
- **Microsoft 365 Copilot** — declarative agent + AI Plugin (OpenAPI v2.4) as the conversational interface
- **Microsoft 365 Agents Toolkit** — provisioning, packaging, and deployment of the declarative agent
- **Adaptive Cards 1.4** — custom response templates for all four actions
- **FastAPI (Python)** — backend "EduDesk IT Agent API" serving mock device, user, and ticket data
- **VS Code Dev Tunnel** — exposes the local FastAPI server to Microsoft 365 Copilot during development

## Impact
For a small charter school IT team, EduDesk collapses several manual lookup steps into a single conversational interface already embedded in staff's daily tools — faster triage, fewer context switches, and a lower barrier for non-technical staff to self-serve basic status checks before escalating to IT.

## Repo & demo
- GitHub: https://github.com/nimsalim/edudesk-agent
- Demo video: _add link after upload_
