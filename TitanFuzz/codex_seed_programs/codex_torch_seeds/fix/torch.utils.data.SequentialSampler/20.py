'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
import torch
data_source = list(range(10))
sampler = torch.utils.data.SequentialSampler(data_source)
print(sampler)
print(sampler.__iter__())
print(sampler.__len__())