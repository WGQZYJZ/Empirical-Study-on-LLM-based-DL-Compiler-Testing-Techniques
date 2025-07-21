'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
import numpy as np
input_tensor = torch.rand(4, 4)
print(input_tensor)
mask = torch.ByteTensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
print(mask)
source = torch.rand(4)
print(source)
torch.Tensor.masked_scatter_(input_tensor, mask, source)
print(input_tensor)