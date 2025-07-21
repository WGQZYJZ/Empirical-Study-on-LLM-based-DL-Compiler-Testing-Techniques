'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
data = torch.arange(0, 100)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.SequentialSampler(data), batch_size=10, drop_last=True)
for batch_indices in batch_sampler:
    print(batch_indices)