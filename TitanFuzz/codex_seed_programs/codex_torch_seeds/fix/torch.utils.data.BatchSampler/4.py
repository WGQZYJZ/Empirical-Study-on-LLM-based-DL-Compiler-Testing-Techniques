'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch.utils.data
import torch
data = torch.arange(0, 100)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.RandomSampler(data), batch_size=10, drop_last=False)
for i in batch_sampler:
    print(i)