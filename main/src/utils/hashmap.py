import os
import csv
from typing import Dict, List

def load_crime_data(file_path: str) -> Dict[str, Dict]:
    """
    Load crime data from CSV file using the correct column names.
    
    Args:
        file_path (str): Relative path to the CSV file from project root
        
    Returns:
        Dict[str, Dict]: Dictionary containing crime data by AreaID
    """
    src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root = os.path.dirname(src_dir)
    absolute_path = os.path.join(project_root, file_path)
    
    crime_data = {}
    
    try:
        with open(absolute_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                area_id = row['AreaID']
                # Store single dictionary instead of list of dictionaries
                crime_data[area_id] = {
                    'priority': int(row['Priority']),
                    'requirement': int(row['ResourceRequirement'])  # Changed to match greedy.py
                }
                
        return crime_data
        
    except Exception as e:
        print(f"Error loading crime data: {str(e)}")
        raise

def update_crime_data(crime_data, area_id, new_priority):
    """
    Update the priority of a specific area in the crime data hashmap.
    :param crime_data: Hashmap of crime data.
    :param area_id: ID of the area to update.
    :param new_priority: New priority value.
    """
    if area_id in crime_data:
        crime_data[area_id]['priority'] = new_priority