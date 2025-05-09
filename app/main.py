from fastapi import FastAPI, Query
import subprocess, json
import os

app = FastAPI(title="TFTF Edge API")

# // ./algo 8.487358 124.629950 "Patag Camp Evangelista" 8.484763 124.655977 "USTP" 100 10

from fastapi import FastAPI, Query
import subprocess
import json

app = FastAPI()

# http://127.0.0.1:8000/api/routes?fromLat=8.50881&fromLong=124.64827&fromName=Bonbon&toLat=8.51133&toLong=124.62429&toName=Westbound Bulua Terminal&transMeter=100.50&hour=10

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

        stdout_lines = result.stdout.strip().splitlines()
        
        for line in reversed(stdout_lines):
            try:
                response_data = json.loads(line)
                
                # Extract route coordinates
                route_coordinates = []
                if "Routes" in response_data:
                    for route in response_data["Routes"]:
                        if "Entry Coordinate" in route:
                            route_coordinates.append(route["Entry Coordinate"])
                        if "Exit Coordinate" in route:
                            route_coordinates.append(route["Exit Coordinate"])
                
                # Create a new ordered response
                ordered_response = {
                    "From": response_data.get("From", {}),
                    "To": response_data.get("To", {}),
                    "Transfer Range": response_data.get("Transfer Range", 0),
                    "Routes": response_data.get("Routes", []),
                    "Coordinates": response_data.get("Coordinates", []),
                    "GeoJSON": response_data.get("GeoJSON", {}),
                }
                
                return ordered_response
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