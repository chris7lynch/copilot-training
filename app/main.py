"""FastAPI application that serves a simple Copilot training landing page."""
from pathlib import Path
from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import router as database_router
from vulnerabilities.sql_injection.vulnerable_routes import router as vuln_router

BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATE_DIR = BASE_DIR / "templates"

app = FastAPI(title="Copilot Training Demo")

# Include database router for vulnerable endpoints training
app.include_router(database_router)
# Include SQL injection vulnerability training module
app.include_router(vuln_router)

# Serve static assets like CSS and JavaScript from the /static path
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

COPILOT_TIPS: List[str] = [
    "Pair Copilot with clear, concise comments to steer code generation.",
    "Review AI-suggested code with the same scrutiny as human PRs.",
    "Use Copilot chat to iterate on tests before refactoring logic.",
]


@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request) -> HTMLResponse:
    """Render the Copilot training home page."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tips": COPILOT_TIPS,
        },
    )


@app.get("/healthz", response_class=HTMLResponse)
async def healthcheck() -> dict[str, str]:
    """Lightweight endpoint that can be used by uptime checks."""
    return {"status": "ok"}
