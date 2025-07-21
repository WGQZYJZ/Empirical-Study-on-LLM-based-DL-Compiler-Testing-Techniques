'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
import torch.utils.data
weights = [1, 2, 3, 4, 5]
sampler = torch.utils.data.WeightedRandomSampler(weights, 5, replacement=True)
for i in range(5):
    print(next(iter(sampler)))