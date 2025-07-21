'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
from torch.nn import Flatten
import torch
from torch.nn import Flatten
input = torch.randn(1, 3, 224, 224)
flatten = Flatten()
output = flatten(input)
print(output.shape)
flatten = Flatten(start_dim=1, end_dim=(- 1))
output = flatten(input)
print(output.shape)