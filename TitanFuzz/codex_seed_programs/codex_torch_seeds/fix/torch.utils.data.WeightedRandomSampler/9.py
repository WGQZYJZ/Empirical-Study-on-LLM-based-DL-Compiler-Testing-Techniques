'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
import torch
weights = [0.2, 0.3, 0.5]
num_samples = 10
replacement = True
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement)
for i in range(10):
    print(next(iter(sampler)))