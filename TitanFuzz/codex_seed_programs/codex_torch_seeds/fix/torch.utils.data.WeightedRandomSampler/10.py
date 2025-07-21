'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.WeightedRandomSampler\ntorch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)\n'
import torch
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
num_samples = 5
replacement = True
generator = None
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement, generator)
print('The result is: ', sampler)
print('The type of result is: ', type(sampler))