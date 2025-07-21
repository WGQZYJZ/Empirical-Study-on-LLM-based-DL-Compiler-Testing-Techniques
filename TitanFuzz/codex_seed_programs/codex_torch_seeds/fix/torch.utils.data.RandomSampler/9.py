'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
import numpy as np
import torch
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sampler = torch.utils.data.RandomSampler(data, replacement=False, num_samples=5)
print(sampler)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
import numpy as np
import torch
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])