'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
sampler = torch.utils.data.WeightedRandomSampler(weights, 10)
for i in range(10):
    print(sampler.__iter__().__next__())