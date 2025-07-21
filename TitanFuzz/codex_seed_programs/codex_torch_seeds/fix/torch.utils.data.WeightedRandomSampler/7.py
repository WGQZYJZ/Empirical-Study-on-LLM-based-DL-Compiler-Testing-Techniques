'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
import numpy as np
weights = np.array([0.5, 0.5])
num_samples = 10
replacement = True
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement)
for (i, index) in enumerate(sampler):
    print('{}: {}'.format(i, index))