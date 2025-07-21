'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
import torch.utils.data
import numpy as np
import torch
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
weights = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sampler = torch.utils.data.WeightedRandomSampler(weights, 5)
for i in range(5):
    print(next(iter(sampler)))