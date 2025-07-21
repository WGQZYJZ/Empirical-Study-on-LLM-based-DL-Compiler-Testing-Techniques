'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
import torch
data = list(range(10))
sampler = torch.utils.data.SequentialSampler(data)
for index in sampler:
    print(index)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=True, num_samples=None)\n'
import torch
import torch
data = list(range(10))
sampler = torch.utils.data.RandomSampler(data)
for index in sampler:
    print(index)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices)\n'
import torch
import torch