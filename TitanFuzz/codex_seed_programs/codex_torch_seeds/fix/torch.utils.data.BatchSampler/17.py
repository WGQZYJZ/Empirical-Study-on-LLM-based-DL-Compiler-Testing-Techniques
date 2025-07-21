'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
input_data = torch.rand(10)
batch_size = 3
batch_sampler = torch.utils.data.BatchSampler(input_data, batch_size, drop_last=False)
for i in batch_sampler:
    print(i)