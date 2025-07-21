'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
from torch.utils.data import Subset
import torch
dataset = torch.randn(20, 10)
indices = torch.tensor([3, 6, 9, 12, 15, 18])
subset = Subset(dataset, indices)
print(subset)