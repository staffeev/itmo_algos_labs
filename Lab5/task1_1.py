import nevergrad as ng


# Problem setup.
weights = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
values = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
bin_capacities = [100, 100, 100, 100, 100]

# Solver variables.
n_bins = len(bin_capacities)
n_items = len(weights)
bins = list(range(n_bins + 1))
variables = [ng.p.Choice(bins) for _ in range(n_items)]

def objective(*assignments):
    value = 0
    bin_weights = [0] * n_bins
    for i_item, assigned_bin in enumerate(assignments):
        if assigned_bin != n_bins:  # Ignore items not assigned to any bin.
            value += values[i_item]
            bin_weights[assigned_bin] += weights[i_item]

    # Constraint violation reduces value.
    fill = [weight - capacity for weight, capacity in zip(bin_weights, bin_capacities)]
    overfill = sum([max(x, 0) for x in fill])
    value -= overfill * sum(bin_capacities)

    return -1 * value

parametrization = ng.p.Instrumentation(*variables)
optimizer = ng.optimizers.DiscreteOnePlusOne(
    parametrization=parametrization,
    budget=5000,
)

recommendation = optimizer.minimize(objective)

best_assignment = recommendation.value[0]
best_value = -1 * objective(*best_assignment)
print(best_value)