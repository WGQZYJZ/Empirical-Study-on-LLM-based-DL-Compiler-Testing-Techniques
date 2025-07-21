'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Sampler\ntorch.utils.data.Sampler(data_source)\n'
import torch
import torch
data = torch.arange(0, 100)
print(data)
sampler = torch.utils.data.Sampler(data)
print(sampler)