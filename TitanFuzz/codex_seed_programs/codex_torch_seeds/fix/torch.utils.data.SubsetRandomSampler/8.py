'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
import torch
data = torch.randn(20, 3)
indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sampler = torch.utils.data.SubsetRandomSampler(indices)
for i in sampler:
    print(i)