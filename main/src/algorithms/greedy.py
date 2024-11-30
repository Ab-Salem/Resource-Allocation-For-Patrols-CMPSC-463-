def greedy_allocation(crime_data, total_resources):
    """
    Perform resource allocation using a greedy algorithm.
    :param crime_data: Hashmap of crime data.
    :param total_resources: Total resources available for allocation.
    :return: Allocation hashmap and total priority covered.
    """
    # Sort areas by priority-to-requirement ratio in descending order
    sorted_areas = sorted(
        crime_data.items(),
        key=lambda item: item[1]['priority'] / item[1]['requirement'],
        reverse=True
    )

    allocation = {}
    total_priority_covered = 0

    # Allocate resources greedily
    for area_id, data in sorted_areas:
        if total_resources >= data['requirement']:
            allocation[area_id] = data['requirement']
            total_resources -= data['requirement']
            total_priority_covered += data['priority']

    return allocation, total_priority_covered
