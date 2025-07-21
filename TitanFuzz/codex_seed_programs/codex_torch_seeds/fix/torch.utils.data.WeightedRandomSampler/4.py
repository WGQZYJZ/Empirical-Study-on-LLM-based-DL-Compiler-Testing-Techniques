'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
import numpy as np
weights = np.array([0.1, 0.2, 0.3, 0.4])
sampler = torch.utils.data.WeightedRandomSampler(weights, 4)
for idx in sampler:
    print(idx)