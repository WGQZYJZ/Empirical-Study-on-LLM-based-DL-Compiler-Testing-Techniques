'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch
input_data = torch.rand(100, 1)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.RandomSampler(input_data), batch_size=5, drop_last=False)
for batch_indices in batch_sampler:
    print(batch_indices)