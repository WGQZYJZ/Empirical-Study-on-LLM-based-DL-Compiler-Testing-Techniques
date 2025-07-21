'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
import torch.utils.data
weights = [0.1, 0.2, 0.3, 0.4]
samples = [1, 2, 3, 4]
sampler = torch.utils.data.WeightedRandomSampler(weights, 4)
for i in sampler:
    print(samples[i])