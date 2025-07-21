'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
data = torch.arange(0, 10)
batch_sampler = torch.utils.data.BatchSampler(torch.utils.data.sampler.SequentialSampler(data), batch_size=3, drop_last=False)
for batch in batch_sampler:
    print(batch)