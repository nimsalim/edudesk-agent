# EduDesk Demo Script

**Total runtime target: ~90 seconds**

---

## Intro (5-10 sec)

"Hi, I'm [name], and this is EduDesk — a declarative agent for Microsoft 365 Copilot that acts as an IT helpdesk assistant for charter schools. It connects Copilot directly to our school's device, user, and ticketing systems through a custom API. Let me walk you through a typical support scenario."

---

## Step 1 — Get user Sarah Johnson (15 sec)

*Type: "Get user Sarah Johnson"*

"Let's say a teacher, Sarah Johnson, calls IT saying her Chromebook won't connect to WiFi. First, EduDesk looks up her account — we can see she's an active, licensed 3rd grade teacher who logged in just a few days ago. So her account isn't the problem."

---

## Step 2 — Get device 5XJ9K2L (15 sec)

*Type: "Get device 5XJ9K2L"*

"Next, EduDesk pulls up the Chromebook assigned to her — serial 5XJ9K2L, device CHR-001, located in Room 204. It's active and properly assigned, so the device itself looks fine too. That points us toward a connectivity issue."

---

## Step 3 — Get TKT-001 (15 sec)

*Type: "Get TKT-001"*

"And sure enough — EduDesk finds there's already an open ticket for this exact issue: Sarah's Chromebook not connecting to school WiFi in Room 204. Instead of creating a duplicate, it surfaces the existing ticket and confirms IT is already on it."

---

## Step 4 — Submit a new ticket (20 sec)

*Type: "Submit a ticket for Marcus Williams - his account is disabled and he can't log into Google Classroom for PE class"*

"Now for a different issue — Marcus Williams in PE has a disabled account and can't get into Google Classroom. EduDesk creates a brand new ticket on the spot, categorizes it, assigns it to the IT team, and confirms it back to the user — all without anyone touching a ticketing portal."

---

## Closing (10-15 sec)

"That's EduDesk — one agent inside Microsoft 365 Copilot that can look up users, check devices, review tickets, and file new ones, all through natural conversation. For a small charter school IT team, this means faster triage and fewer steps between 'something's broken' and 'it's logged.' Thanks for watching!"

---

## Notes for recording

- Pause ~3-5 seconds after each query to let the adaptive card fully render before talking over it.
- If TKT-001 or other ticket numbers differ from a prior run, just read what's on screen — the script describes the expected data, not hardcoded screen text.
- Keep tone conversational, not scripted-sounding — it's fine to paraphrase slightly.
