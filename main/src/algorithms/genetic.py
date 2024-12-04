import random

def genetic_allocation(crime_data, total_resources, population_size=100, generations=50):
    """
    Improved genetic algorithm approach for resource allocation.
    Maximizes resource utilization while optimizing for priority.
    """
    def create_individual():
        """Create an individual that tries to use maximum resources possible"""
        individual = {}
        remaining_resources = total_resources
        # Convert to list and sort by priority/requirement ratio for better initial solutions
        areas = list(crime_data.items())
        areas.sort(key=lambda x: x[1]['priority']/x[1]['requirement'], reverse=True)
        
        for area_id, data in areas:
            req = data['requirement']
            if req <= remaining_resources:
                individual[area_id] = req
                remaining_resources -= req
        return individual

    def fitness(individual):
        """
        Calculate fitness with bonus for using more resources
        """
        priority_sum = sum(crime_data[area]['priority'] for area in individual)
        resources_used = sum(individual.values())
        resource_usage_ratio = resources_used / total_resources
        return priority_sum * (1 + resource_usage_ratio)  # Bonus for using more resources

    # Create initial population
    population = [create_individual() for _ in range(population_size)]

    for gen in range(generations):
        # Sort by fitness
        population.sort(key=fitness, reverse=True)
        
        # Keep top 20%
        new_pop = population[:population_size//5]
        
        while len(new_pop) < population_size:
            # Tournament selection
            parent1, parent2 = random.sample(population[:50], 2)
            
            # Crossover
            child = {}
            all_areas = set(parent1.keys()) | set(parent2.keys())
            
            # Try to include areas from both parents while respecting resource constraint
            remaining_resources = total_resources
            for area in sorted(all_areas, 
                             key=lambda x: crime_data[x]['priority']/crime_data[x]['requirement'],
                             reverse=True):
                req = crime_data[area]['requirement']
                if req <= remaining_resources:
                    child[area] = req
                    remaining_resources -= req
            
            # Mutation: try to fill any remaining resources
            if remaining_resources > 0:
                unused_areas = set(crime_data.keys()) - set(child.keys())
                for area in sorted(unused_areas,
                                 key=lambda x: crime_data[x]['priority']/crime_data[x]['requirement'],
                                 reverse=True):
                    req = crime_data[area]['requirement']
                    if req <= remaining_resources:
                        child[area] = req
                        remaining_resources -= req
            
            new_pop.append(child)
        
        population = new_pop

    # Get best solution
    best_solution = max(population, key=fitness)
    return best_solution, sum(crime_data[area]['priority'] for area in best_solution)