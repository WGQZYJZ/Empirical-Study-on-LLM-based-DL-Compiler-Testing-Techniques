'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
from torch.utils.data import WeightedRandomSampler
weights = torch.Tensor([0.2, 0.8])
num_samples = 5
sampler = WeightedRandomSampler(weights, num_samples, replacement=True)
for idx in sampler:
    print(idx)