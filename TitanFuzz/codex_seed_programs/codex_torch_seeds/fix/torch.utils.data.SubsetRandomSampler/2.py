'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
import torch.utils.data
import numpy as np
import torch
data = np.arange(20)
print(data)
sampler = torch.utils.data.SubsetRandomSampler(indices=[1, 3, 5, 7, 9])
for (i, index) in enumerate(sampler):
    print('index: {} data: {}'.format(index, data[index]))