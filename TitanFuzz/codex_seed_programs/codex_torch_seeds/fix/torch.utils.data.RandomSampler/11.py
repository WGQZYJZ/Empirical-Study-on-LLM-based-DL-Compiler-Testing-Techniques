'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
input_data = torch.rand(5)
sampler = torch.utils.data.RandomSampler(input_data)
for i in sampler:
    print(i)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
input_data = torch.rand(5)
sampler = torch.utils.data.SequentialSampler(input_data)
for i in sampler:
    print(i)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices)\n'
import torch
input_data = torch.rand(5)
indices = [1, 3]
sampler = torch.utils.data.SubsetRandomSampler(indices)