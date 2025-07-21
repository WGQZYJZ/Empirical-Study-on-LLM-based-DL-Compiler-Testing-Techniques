'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
import numpy as np
data_size = 100
data = np.random.rand(data_size, 3)
indices = np.random.choice(data_size, size=int((data_size * 0.8)), replace=False)
indices_test = np.array(list((set(range(data_size)) - set(indices))))
sampler = torch.utils.data.SubsetRandomSampler(indices)
sampler_test = torch.utils.data.SubsetRandomSampler(indices_test)
print('Test 1: ', indices.shape)
print('Test 2: ', indices_test.shape)