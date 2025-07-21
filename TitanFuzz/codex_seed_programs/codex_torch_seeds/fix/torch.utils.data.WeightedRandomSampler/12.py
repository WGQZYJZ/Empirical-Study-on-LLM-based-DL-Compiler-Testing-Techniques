'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
sampler = torch.utils.data.WeightedRandomSampler(weights, 5)
print('Sampler: ', sampler)
for idx in sampler:
    print('Index: ', idx)