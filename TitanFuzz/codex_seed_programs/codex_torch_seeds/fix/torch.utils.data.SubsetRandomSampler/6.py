'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
from torch.utils.data import DataLoader, SubsetRandomSampler
input_data = torch.randn(10, 2)
sampler = SubsetRandomSampler(list(range(5)))
dataloader = DataLoader(input_data, batch_size=2, sampler=sampler)
for batch in dataloader:
    print(batch)