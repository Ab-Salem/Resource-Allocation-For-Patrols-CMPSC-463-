import argparse
from utils.hashmap import load_crime_data
from algorithms.greedy import greedy_allocation

def main(algorithm, resource_limit):
    # Load crime data
    crime_data = load_crime_data('data/crime_data.csv')

    if algorithm == 'greedy':
        allocation, total_priority = greedy_allocation(crime_data, resource_limit)
        print("\nResource Allocation Results (Greedy Algorithm):")
        for area, allocated in allocation.items():
            print(f"  - Area {area}: Allocated {allocated} units")
        print(f"Total Priority Covered: {total_priority}")
    else:
        print("Unsupported algorithm. Please use 'greedy'.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Resource Allocation for Patrols")
    parser.add_argument('--algorithm', type=str, default='greedy',
                        help="Algorithm to use (greedy or dp)")
    parser.add_argument('--resources', type=int, default=10,
                        help="Total resources available for allocation")
    args = parser.parse_args()

    main(algorithm=args.algorithm, resource_limit=args.resources)
