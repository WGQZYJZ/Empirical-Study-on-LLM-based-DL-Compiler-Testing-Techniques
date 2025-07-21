'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Sampler\ntorch.utils.data.Sampler(data_source)\n'
import torch
import numpy as np
import torch
data = np.arange(10)
sampler = torch.utils.data.Sampler(data)
print(sampler)