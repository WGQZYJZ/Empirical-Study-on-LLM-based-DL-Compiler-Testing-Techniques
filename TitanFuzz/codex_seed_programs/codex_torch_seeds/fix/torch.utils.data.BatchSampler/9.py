'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch
data = torch.randint(low=0, high=100, size=(20,))
print(f'data: {data}')
sampler = torch.utils.data.BatchSampler(torch.utils.data.RandomSampler(data), batch_size=5, drop_last=False)
print(f'sampler: {sampler}')
for batch in sampler:
    print(f'batch: {batch}')
    print(f'data[batch]: {data[batch]}')