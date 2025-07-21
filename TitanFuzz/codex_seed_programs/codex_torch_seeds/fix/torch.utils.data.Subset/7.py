'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
import torch
data = torch.arange(0, 10)
sampler = torch.utils.data.Subset(data, [2, 4, 6, 8])
print(sampler)