'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
from torch.utils.data import BatchSampler
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampler = BatchSampler(input_data, batch_size=4, drop_last=False)
for i in sampler:
    print(i)