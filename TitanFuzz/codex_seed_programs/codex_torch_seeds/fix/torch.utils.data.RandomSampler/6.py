'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
import torch.utils.data
import numpy as np
print('PyTorch version: ', torch.__version__)
data = np.random.randint(0, 100, size=(100,))
print('Input data: ', data)
random_sampler = torch.utils.data.RandomSampler(data)
for i in random_sampler:
    print('Index: ', i)