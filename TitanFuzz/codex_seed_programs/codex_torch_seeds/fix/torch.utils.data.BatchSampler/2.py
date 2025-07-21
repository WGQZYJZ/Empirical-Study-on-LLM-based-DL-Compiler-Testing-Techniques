'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch
data = list(range(10))
sampler = torch.utils.data.BatchSampler(data, batch_size=2, drop_last=True)
for batch in sampler:
    print(batch)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch
data = list(range(10))
sampler = torch.utils.data.BatchSampler(data, batch_size=2, drop_last=False)