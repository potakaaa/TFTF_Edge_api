from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json
import os

app = FastAPI(title="TFTF Edge API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/routes")
async def find_route(
    fromLat: float = Query(...),
    fromLong: float = Query(...),
    toLat: float = Query(...),
    toLong: float = Query(...),
):
    request_payload = {
        "start": {"lat": fromLat, "lon": fromLong},
        "end": {"lat": toLat, "lon": toLong}
    }

    try:
        proc = subprocess.Popen(
            ["./app/runner.exe"],  # Correct path
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = proc.communicate(json.dumps(request_payload) + "\n")

        # Try to parse from last valid line in output
        lines = stdout.strip().splitlines()
        for line in reversed(lines):
            try:
                return json.loads(line.strip())
            except json.JSONDecodeError:
                continue

        return {
            "error": "No valid JSON found in runner output",
            "raw_output": lines,
            "stderr": stderr,
        }

    except Exception as e:
        return {
            "error": "Subprocess failed",
            "details": str(e)
        }
