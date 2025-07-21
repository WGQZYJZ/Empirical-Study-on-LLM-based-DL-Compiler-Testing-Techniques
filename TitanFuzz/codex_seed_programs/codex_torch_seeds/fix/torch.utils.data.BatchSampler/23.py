'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch.utils.data
import torch
import torch.utils.data
data = torch.arange(1, 11)
batch_size = 3
sampler = torch.utils.data.BatchSampler(data, batch_size, drop_last=False)
for batch in sampler:
    print(batch)