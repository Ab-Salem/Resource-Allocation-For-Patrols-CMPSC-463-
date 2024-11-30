# **Resource Allocation for Patrols**

## **Overview**
This project implements a system to optimize the allocation of resources such as patrol units or surveillance cameras to high-crime areas. The primary goal is to maximize coverage and efficiency while considering limited resources. The system utilizes:
- A **Greedy Algorithm** for rapid decision-making.
- **Dynamic Programming** for scenarios requiring comprehensive optimization.
- **Hashmaps** to store and manage cluster information, resource allocations, and coverage data.

---

## **Key Features**
1. **Efficient Resource Allocation**: Optimally allocate patrol units to high-priority areas.
2. **Dynamic Updates**: Adapt to new crime data in real-time.
3. **Data Management with Hashmaps**:
   - Fast lookups for high-crime areas.
   - Efficient tracking of resource allocation and remaining capacities.
4. **Scalable Design**: Supports large datasets with real-time decision-making capabilities.

---

## **Use Cases**
1. **Patrol Unit Assignment**:
   - Deploy limited police patrol units to maximize high-crime area coverage.
2. **Surveillance Optimization**:
   - Allocate surveillance cameras to critical zones.
3. **Dynamic Resource Reallocation**:
   - Reassign resources as new crime data becomes available.

---

## **Algorithmic Approach**

### **1. Greedy Algorithm**
- **Purpose**: Quickly allocate resources by prioritizing areas with the highest priority-to-cost ratio.
- **Steps**:
  1. Sort areas by their priority-to-cost ratio (e.g., crime severity per patrol time required).
  2. Allocate resources incrementally to the most efficient areas until resources are exhausted.
  3. Use a hashmap to track allocated areas and remaining resource capacities.

### **2. Dynamic Programming**
- **Purpose**: For cases where constraints are complex (e.g., budget limits, overlapping priorities).
- **Steps**:
  1. Define a state space representing resource allocation combinations.
  2. Use a hashmap to store intermediate results (memoization) for fast lookups.
  3. Solve the problem recursively or iteratively to find the optimal allocation.

---

## **Project Structure**
```plaintext
|-- src/
|   |-- main.py             # Main implementation script
|   |-- algorithms/
|   |   |-- greedy.py       # Greedy algorithm implementation
|   |   |-- dynamic_programming.py # Dynamic programming implementation
|   |-- utils/
|       |-- hashmap_utils.py # Hashmap utilities for data storage and lookup
|-- data/
|   |-- crime_data.csv       # Input crime data (location, priority, resource requirement)
|-- README.md                # Project documentation
```

---

## **Setup Instructions**

### **Prerequisites**
1. Python 3.8+ installed.
2. Libraries:
   - `pandas` for data handling.
   - `numpy` for numerical operations.
   - `matplotlib` for visualization (optional).

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/resource-allocation-patrols.git
   ```
2. Navigate to the project directory:
   ```bash
   cd resource-allocation-patrols
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **Step 1: Input Data**
Prepare a CSV file (`data/crime_data.csv`) with the following columns:
- `AreaID`: Unique identifier for the area.
- `Priority`: Crime severity score.
- `ResourceRequirement`: Number of patrol units or hours needed.

Example:
```csv
AreaID,Priority,ResourceRequirement
101,50,3
102,40,2
103,60,5
```

### **Step 2: Run the Program**
To use the **Greedy Algorithm**:
```bash
python src/main.py --algorithm greedy
```

To use **Dynamic Programming**:
```bash
python src/main.py --algorithm dp
```

### **Step 3: Results**
- View allocation results in the terminal.
- Output includes:
  - Areas covered.
  - Total resources allocated.
  - Efficiency metrics.

---

## **How Hashmaps Are Used**
1. **Crime Data Management**:
   - Store area details indexed by `AreaID` for fast lookups:
     ```python
     crime_data = {101: {'priority': 50, 'requirement': 3}, ...}
     ```

2. **Allocation Tracking**:
   - Track resources allocated to each area:
     ```python
     allocation = {101: 3, 102: 2}
     ```

3. **Dynamic Programming Memoization**:
   - Use hashmaps to store intermediate results for overlapping subproblems.

4. **Real-Time Updates**:
   - Quickly update area priorities and allocations as new data arrives.

---

## **Example Output**
### Input:
```plaintext
Total resources available: 6 units
Areas:
    - Area 101: Priority 50, Requirement 3
    - Area 102: Priority 40, Requirement 2
    - Area 103: Priority 60, Requirement 5
```

### Output (Greedy):
```plaintext
Allocated resources:
    - Area 102: 2 units (Score: 40)
    - Area 101: 3 units (Score: 50)
Remaining resources: 1 unit
Total priority score covered: 90
```

---

## **Future Enhancements**
1. Integrate machine learning to dynamically predict crime patterns.
2. Add support for multi-objective optimization (e.g., minimizing travel time).
3. Include visualization of patrol routes on a map.

---

## **Contributors**
- Your Name (your.email@example.com)

