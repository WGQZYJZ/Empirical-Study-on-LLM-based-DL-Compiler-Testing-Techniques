'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
from torch.utils.data import WeightedRandomSampler
weights = [0.1, 0.2, 0.7]
samples = [1, 2, 3]
sampler = WeightedRandomSampler(weights, 2)
for i in sampler:
    print(samples[i])