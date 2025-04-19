from fastapi import FastAPI, Query
import subprocess, json

app = FastAPI(title="TFTF Edge API")

# // ./algo 8.487358 124.629950 "Patag Camp Evangelista" 8.484763 124.655977 "USTP" 100 10

from fastapi import FastAPI, Query
import subprocess
import json

app = FastAPI()

@app.get("/api/routes")
async def findRoute(
    fromLat: float = Query(...),
    fromLong: float = Query(...),
    fromName: str = Query(...),
    toLat: float = Query(...),
    toLong: float = Query(...),
    toName: str = Query(...),
    transMeter: float = Query(...),
    hour: int = Query(...)
):
    geojsonPath = "./app/routes.geojson"  # Adjust this path as needed
    import os
    print("Current working directory:", os.getcwd())

    

    try:
        result = subprocess.run(
            ["./app/algo", str(fromLat), str(fromLong), fromName, str(toLat), str(toLong), toName, str(transMeter), str(hour), geojsonPath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        print(geojsonPath)
        # try:
        #     response_data = json.loads(result.stdout)
        #     return response_data
        # except json.JSONDecodeError as e:
        #     return {"error": "Invalid JSON output", "stdout": result.stdout, "stderr": result.stderr}

        stdout_lines = result.stdout.strip().splitlines()
        # print("Raw output:", result.stdout)  # Debugging line
        for line in reversed(stdout_lines):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue

        return {
            "error": "Could not parse JSON output from C++ program",
            "stdout": result.stdout,
            "stderr": result.stderr,
        }

    except subprocess.CalledProcessError as e:
        return {
            "error": "Execution failed",
            "details": str(e),
            "stderr": e.stderr
        }



    #  try:
    #     output = subprocess.check_output(["./app/algorithm", str(a), str(b)])
    #     data = json.loads(output.decode("utf-8"))
    #     return data
    # except subprocess.CalledProcessError as e:
    #     return {"error": f"Execution failed: {e}"}
    # except json.JSONDecodeError:
    #     return {"error": "Invalid JSON output from C++ program"}