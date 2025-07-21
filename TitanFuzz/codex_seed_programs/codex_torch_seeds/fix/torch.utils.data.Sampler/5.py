'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Sampler\ntorch.utils.data.Sampler(data_source)\n'
import torch
import torch.utils.data
import torch
import torch.utils.data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampler = torch.utils.data.Sampler(data)
print(sampler)