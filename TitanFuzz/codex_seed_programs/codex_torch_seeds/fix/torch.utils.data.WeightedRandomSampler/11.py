'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
import numpy as np
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_samples = 10
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)
print(sampler)