import argparse
import os
from utils.hashmap import load_crime_data
from algorithms.greedy import greedy_allocation
from algorithms.genetic import genetic_allocation
from utils.visualize import visualize_allocation, save_visualization

def main(algorithm, resource_limit):
    # Create output directory if it doesn't exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load crime data
    crime_data = load_crime_data('data/crime_data.csv')

    # Dictionary of available algorithms
    algorithms = {
        'greedy': (greedy_allocation, 'Greedy'),
        'genetic': (genetic_allocation, 'Genetic')
    }

    if algorithm in algorithms:
        algo_func, algo_name = algorithms[algorithm]
        
        # Run the selected algorithm
        allocation, total_priority = algo_func(crime_data, resource_limit)
        
        # Print results
        print(f"\nResource Allocation Results ({algo_name} Algorithm):")
        print("\nDetailed Allocation:")
        for area, allocated in allocation.items():
            priority = crime_data[area]['priority']
            print(f"  - Area {area}: Allocated {allocated} units (Priority: {priority})")
        print(f"\nTotal Priority Covered: {total_priority}")
        
        # Create and save visualization
        output_file = f'{algorithm}_allocation_visualization.png'
        fig = visualize_allocation(crime_data, allocation, resource_limit, algo_name)
        save_visualization(fig, os.path.join(output_dir, output_file))
        print(f"\nVisualization saved to {output_dir}/{output_file}")

        # Print summary statistics
        resources_used = sum(allocation.values())
        print("\nAllocation Summary:")
        print(f"Total Resources Used: {resources_used}/{resource_limit}")
        print(f"Resource Utilization: {(resources_used/resource_limit)*100:.2f}%")
        print(f"Areas Covered: {len(allocation)}/{len(crime_data)}")
        print(f"Coverage Ratio: {(len(allocation)/len(crime_data))*100:.2f}%")
        
    else:
        print(f"Unsupported algorithm. Please use one of: {', '.join(algorithms.keys())}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Resource Allocation for Patrols")
    parser.add_argument('--algorithm', type=str, default='greedy',
                        help="Algorithm to use (greedy or genetic)")
    parser.add_argument('--resources', type=int, default=600,
                        help="Total resources available for allocation")
    args = parser.parse_args()

    main(algorithm=args.algorithm, resource_limit=args.resources)