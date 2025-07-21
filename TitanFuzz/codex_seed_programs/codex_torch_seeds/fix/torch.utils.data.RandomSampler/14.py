'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
import torch.utils.data
import numpy as np
data_source = np.random.randint(1, 100, (100,))
sampler = torch.utils.data.RandomSampler(data_source)
print('The result is: ', sampler)