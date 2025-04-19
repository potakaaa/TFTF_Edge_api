# TFTFEdge API 🚏

Welcome to **TFTFEdge API**, a cutting-edge API designed to help you navigate the jeepney routes of Cagayan de Oro (and other cities with jeepney networks). This tool allows developers to easily integrate real-time route suggestions based on user inputs such as starting and destination points, transfer range, and time of travel.

With TFTFEdge, you can empower your applications to recommend optimized jeepney routes, helping commuters navigate through their cities efficiently!

---

## 🚀 Features
- **Route Calculation:** Efficient route finding based on user-specified start and destination points.
- **GeoJSON Integration:** Loads real-time route data from GeoJSON files for flexibility in different cities.
- **Transfer Cost & Time Optimization:** Provides recommendations with calculated transfer costs and estimated times.

---

## 🛠️ Technologies Used
- **FastAPI** for creating a fast, modern web API.
- **Python Subprocess** to communicate with C++ route algorithms.
- **GeoJSON** for flexible and easy-to-manage route data.
- **C++** for route pathfinding algorithm implementation.

---

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TFTFEdge.git
   cd TFTFEdge
   ```

2. Install dependencies (make sure to use a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure your C++ algorithm (`algo`) is compiled and available in the project directory.

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## 🛤️ Sample Route Query

### Example Request:
```bash
GET /api/routes?fromLat=8.50881&fromLong=124.64827&fromName=Bonbon&toLat=8.51133&toLong=124.62429&toName=Westbound Bulua Terminal&transMeter=100.5&hour=10
```

### Sample Response:
```json
{
  "From": {
    "Lattitude": 8.50881,
    "Longitude": 124.64827,
    "Origin Name": "Bonbon"
  },
  "Routes": [
    {
      "Route ID": 7,
      "Route Name": "Bonbon (R1) – Cogon Public Market",
      "Transfer Cost": 0.0,
      "Entry Coordinate": [8.50881, 124.64827],
      "Exit Coordinate": [8.47759, 124.64866]
    },
    {
      "Route ID": 7,
      "Route Name": "Bulua (R4) – Cogon Public Market",
      "Transfer Cost": 0.0,
      "Entry Coordinate": [8.47759, 124.64866],
      "Exit Coordinate": [8.47759, 124.64866]
    },
    {
      "Route ID": 7,
      "Route Name": "Bulua (R4) – Cogon Public Market",
      "Transfer Cost": 0.0,
      "Entry Coordinate": [8.47759, 124.64866],
      "Exit Coordinate": [8.51133, 124.62429]
    }
  ],
  "To": {
    "Destination Name": "Westbound Bulua Terminal",
    "Lattitude": 8.51133,
    "Longitude": 124.62429
  },
  "Transfer Range": 100.5
}
```

---

## 🌍 Contributing

We welcome contributions! If you find bugs or have ideas for improvements, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
