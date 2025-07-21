'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import torch.utils.data
input_data = torch.randn(10, 3, 32, 32)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.SequentialSampler(range(10)), batch_size=3, drop_last=True)
for indices in batch_sampler:
    print(indices)
    print(input_data[indices])