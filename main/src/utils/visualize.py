import matplotlib.pyplot as plt
import numpy as np

def visualize_allocation(crime_data, allocation, total_resources, algorithm_name):
    """
    Create visualization for resource allocation results.
    Shows priority vs resource allocation, and creates a heatmap of covered areas.
    """
    # Create figure with multiple subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Resource Allocation Analysis - {algorithm_name} Algorithm', fontsize=16)

    # First subplot: Priority vs Resource Allocation
    covered_areas = []
    uncovered_areas = []
    
    for area_id, data in crime_data.items():
        if area_id in allocation:
            covered_areas.append((data['priority'], allocation[area_id]))
        else:
            uncovered_areas.append((data['priority'], data['requirement']))

    # Convert to numpy arrays for plotting
    covered = np.array(covered_areas) if covered_areas else np.array([[0, 0]])
    uncovered = np.array(uncovered_areas) if uncovered_areas else np.array([[0, 0]])

    # Scatter plot
    ax1.scatter(covered[:, 1], covered[:, 0], c='green', label='Covered Areas', alpha=0.6)
    ax1.scatter(uncovered[:, 1], uncovered[:, 0], c='red', label='Uncovered Areas', alpha=0.6)
    ax1.set_xlabel('Resources Required/Allocated')
    ax1.set_ylabel('Priority Level')
    ax1.set_title('Priority vs Resource Allocation')
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend()

    # Second subplot: Coverage Statistics
    coverage_stats = {
        'Total Resources': total_resources,
        'Resources Used': sum(allocation.values()),
        'Areas Covered': len(allocation),
        'Areas Uncovered': len(crime_data) - len(allocation),
    }

    # Create bar chart
    bars = ax2.bar(coverage_stats.keys(), coverage_stats.values())
    ax2.set_title('Coverage Statistics')
    ax2.set_ylabel('Count')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom')

    plt.tight_layout()
    return fig

def save_visualization(fig, filename):
    """
    Save the visualization to a file
    """
    fig.savefig(filename)
    plt.close(fig)