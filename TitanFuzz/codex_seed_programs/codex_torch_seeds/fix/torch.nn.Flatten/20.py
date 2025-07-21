'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
from torch.nn import Flatten
x = torch.ones(2, 3, 4, 5)
print(x)
flatten = Flatten()
out = flatten(x)
print(out)