'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import numpy as np
input_data = np.arange(20).reshape(10, 2)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.SequentialSampler(input_data), batch_size=3, drop_last=False)
for batch in batch_sampler:
    print(batch)