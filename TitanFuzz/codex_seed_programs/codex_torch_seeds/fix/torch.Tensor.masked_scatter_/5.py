'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
import numpy as np
x = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
source = torch.randn(3, 4)
torch.Tensor.masked_scatter_(x, mask, source)
result = torch.masked_scatter(x, mask, source)
x = torch.randn(3, 4)