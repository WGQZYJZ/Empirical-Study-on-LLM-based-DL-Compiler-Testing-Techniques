'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
import numpy as np
data_source = torch.randn(10)
sampler = torch.utils.data.SequentialSampler(data_source)
for i in sampler:
    print(i)