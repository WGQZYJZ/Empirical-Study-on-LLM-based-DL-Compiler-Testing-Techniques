'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
from torch.utils.data import RandomSampler
data_source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampler = RandomSampler(data_source, num_samples=4)
for i in sampler:
    print(i)