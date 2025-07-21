'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch.utils.data as data
import torch
import torch.utils.data as data
input_data = list(range(20))
print(input_data)
batch_sampler = data.BatchSampler(input_data, batch_size=5, drop_last=False)
for i in batch_sampler:
    print(i)
batch_sampler = data.BatchSampler(input_data, batch_size=5, drop_last=True)
for i in batch_sampler:
    print(i)