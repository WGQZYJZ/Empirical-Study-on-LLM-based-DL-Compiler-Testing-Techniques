'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SequentialSampler\ntorch.utils.data.SequentialSampler(data_source)\n'
import torch
from torch.utils.data import TensorDataset, SequentialSampler
data = torch.randint(0, 100, (5, 2))
labels = torch.randint(0, 2, (5, 1))
sampler = SequentialSampler(data)
for idx in sampler:
    print(idx)