# **Resource Allocation for Police Patrols**

Link to Powerpoint: https://docs.google.com/presentation/d/1tc6zfjo776iIleKq4Qc-Ase5NmZ0tWWqiEHNmh9qW-4/edit?usp=sharing

## **Overview**
This project addresses a critical challenge in law enforcement: optimizing the deployment of police patrol units across different areas of a city to maximize crime prevention and response capabilities. By strategically allocating limited police resources to areas based on their crime rates and priority levels, the system aims to enhance public safety while efficiently utilizing available patrol units.

### **Core Purpose**
- **Optimize Police Coverage**: Strategically distribute patrol units to areas with higher crime rates
- **Maximize Public Safety**: Ensure high-priority areas receive adequate police presence
- **Resource Efficiency**: Make the most effective use of limited police patrol units
- **Data-Driven Deployment**: Base allocation decisions on crime statistics and area priorities

The system utilizes multiple algorithmic approaches:
- A **Greedy Algorithm** for rapid patrol deployment decisions
- A **Genetic Algorithm** for evolving optimal patrol distribution strategies
- **Visual Analytics** to evaluate patrol coverage and effectiveness
- **Efficient Data Management** using hashmaps to track patrol allocations and crime statistics

### **Real-World Application**
This system can help police departments:
- Respond to changing crime patterns by reallocating resources
- Balance coverage between high-crime areas and routine patrol requirements

---


## **Project Structure**
```plaintext
|-- src/
|   |-- main.py             # Main implementation script
|   |-- algorithms/
|   |   |-- greedy.py       # Greedy algorithm implementation
|   |   |-- genetic.py      # Genetic algorithm implementation
|   |-- utils/
|       |-- hashmap.py       # Hashmap utilities for data storage
|       |-- visualize.py     # Visualization 
|-- data/
|   |-- crime_data.csv      # Input crime data
|   |-- generate_data.py      # Generates Sample Crime data
|-- output/                 # Generated visualizations (png's)
|-- README.md              # Project documentation
```

---

## **Setup Instructions**

### **Prerequisites**
1. Python 3.8+ installed
2. Required libraries:
   ```bash
   pip install matplotlib numpy
   ```

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/resource-allocation-patrols.git
   ```
2. Navigate to the project directory:
   ```bash
   cd resource-allocation-patrols
   ```

---

## **Usage**

### **Step 1: Navigate to main directory in repository**
```bash
cd main
```

### **Step 2: Generate Test Data**
Generate sample crime data using the provided script:
```bash
python generate_data.py 
```
This creates a CSV file in the data directory with 300 areas.

### **Step 3: Run the Program**

The program supports different algorithms and resource limits:

```bash
# Run with greedy algorithm (default)
python src/main.py --algorithm greedy --resources 600

# Run with genetic algorithm
python src/main.py --algorithm genetic --resources 600

# Change resource limit
python src/main.py --algorithm greedy --resources 450
```

Command line arguments:
- `--algorithm`: Choose between 'greedy' or 'genetic' (default: 'greedy')
- `--resources`: Set total available resources (default: 600)

### **Step 4: Results**

The program provides:
1. **Terminal Output**:
   - Detailed allocation for each area
   - Total priority covered
   - Resource utilization statistics
   - Coverage ratios

2. **Visualizations** (saved in output/):
   - `greedy_allocation_visualization.png` or
   - `genetic_allocation_visualization.png`

Each visualization includes:
- Priority vs Resource scatter plot
- Coverage statistics bar chart

---

## **Algorithm Comparisons**

### **Greedy Algorithm**
- Quick decision-making
- Optimizes for immediate best choice
- Generally good resource utilization

### **Genetic Algorithm**
- Evolutionary approach
- May find better global solutions
- Balances exploration and exploitation
- Parameters:
  - Population size: 100
  - Generations: 50

---

## **Example Output**

### Terminal Output:
```plaintext
Resource Allocation Results (Greedy Algorithm):
Total Resources Used: 178/180
Resource Utilization: 98.89%
Areas Covered: 45/300
Coverage Ratio: 15.00%
Total Priority Covered: 3245
```

### Visualization:
Two plots are generated:
1. Scatter plot showing:
   - Covered areas (green)
   - Uncovered areas (red)
   - Priority vs Resource distribution
2. Bar chart showing:
   - Total resources available
   - Resources used
   - Areas covered/uncovered

   ![image](https://github.com/user-attachments/assets/6965eb33-60b2-4cde-bc09-341e7f29229e)


---
## **Discussion and Conclusions**

### **Project Achievements**
- Successfully implemented multiple resource allocation algorithms for police patrol optimization
- Developed visualization tools for analyzing patrol coverage
- Created a scalable system handling 300+ patrol areas
- Achieved efficient resource utilization with priority-based allocation

### **Technical Implementation**
Applied key course concepts:
- **Data Structures**: Implemented hashmaps for O(1) lookup of area information
- **Algorithm Design**: Developed greedy and genetic algorithms showcasing different optimization approaches
- **Time Complexity**: Optimized code for handling large datasets efficiently
- **Space Complexity**: Managed memory usage through efficient data structures

### **Limitations and Challenges**

1. **Algorithm Limitations**:
   - Greedy algorithm may miss global optimum solutions
   - Genetic algorithm's randomness affects consistency
   - No guarantee of finding perfect allocation solutions

2. **Real-World Constraints Not Modeled**:
   - Does not consider patrol unit travel time
   - Lacks temporal crime pattern analysis
   - No integration with real-time incident data
   - Doesn't account for overlapping patrol areas

3. **Technical Constraints**:
   - Limited to static priority values
   - No handling of emergency reallocation
   - Simplified resource requirements model

### **Future Work**

1. **Algorithm Improvements**:
   - Implement machine learning for priority prediction
   - Add dynamic programming solution
   - Include multi-objective optimization

2. **Feature Additions**:
   - Real-time data integration
   - Geographic information system (GIS) integration
   - Temporal analysis of crime patterns
   - Interactive visualization dashboard

3. **Real-World Enhancements**:
   - Shift scheduling integration
   - Emergency response considerations
   - Multi-precinct coordination
   - Officer expertise matching

---

## **Contributors**
- Abdallah Salem 
- Murad Shaw 
