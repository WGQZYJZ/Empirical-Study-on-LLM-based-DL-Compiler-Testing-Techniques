'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import numpy as np
import torch
x = np.arange(0, 24).reshape((2, 3, 4))
print('Input data: ', x)
batch_size = 2
sampler = torch.utils.data.BatchSampler(torch.utils.data.SequentialSampler(range(x.shape[0])), batch_size=batch_size, drop_last=False)
for index in sampler:
    print('Batch index: ', index)
    print('Batch data: ', x[index])