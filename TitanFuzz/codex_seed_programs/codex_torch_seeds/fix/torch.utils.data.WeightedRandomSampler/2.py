'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
input_data = torch.randint(0, 100, (10,))
print(input_data)
weights = torch.randint(0, 100, (10,))
weights = (weights / weights.sum())
print(weights)
sampler = torch.utils.data.WeightedRandomSampler(weights, 10, replacement=True)
for i in range(5):
    idx = sampler.__iter__().__next__()
    print(idx)
    print(input_data[idx])