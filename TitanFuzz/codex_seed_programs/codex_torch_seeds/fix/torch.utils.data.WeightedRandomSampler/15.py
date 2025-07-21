'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
from torch.utils.data import WeightedRandomSampler
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampler = WeightedRandomSampler(weights, 3)
for i in range(10):
    print(list(sampler))