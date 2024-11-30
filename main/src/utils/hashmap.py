def load_crime_data(file_path):
    """
    Load crime data from a CSV file into a hashmap.
    :param file_path: Path to the crime data file.
    :return: Hashmap of crime data.
    """
    import csv
    crime_data = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            area_id = int(row['AreaID'])
            crime_data[area_id] = {
                'priority': int(row['Priority']),
                'requirement': int(row['ResourceRequirement'])
            }
    return crime_data


def update_crime_data(crime_data, area_id, new_priority):
    """
    Update the priority of a specific area in the crime data hashmap.
    :param crime_data: Hashmap of crime data.
    :param area_id: ID of the area to update.
    :param new_priority: New priority value.
    """
    if area_id in crime_data:
        crime_data[area_id]['priority'] = new_priority
