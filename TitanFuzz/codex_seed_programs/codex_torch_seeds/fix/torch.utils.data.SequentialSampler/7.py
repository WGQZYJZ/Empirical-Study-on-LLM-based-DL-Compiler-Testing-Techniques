'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
from torch.utils.data import SequentialSampler
data_source = [i for i in range(10)]
sampler = SequentialSampler(data_source)
for i in sampler:
    print(i)